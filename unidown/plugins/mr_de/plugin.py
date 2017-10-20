import re
import traceback
from concurrent.futures import ProcessPoolExecutor
from datetime import datetime
from pathlib import Path

import certifi
import unidown.core.data.static as static_data
import urllib3
import urllib3.util
from unidown.plugins.a_plugin import APlugin
from unidown.plugins.data.link_item import LinkItem
from unidown.plugins.data.plugin_info import PluginInfo
from unidown.plugins.exceptions import GetDownloadLinksException, LastUpdateException
from unidown.plugins.mr_de.exceptions import GetEbookLinksException, NothingFoundInThread
from unidown.plugins.mr_de.html_parser.last_update_html_parser import LastUpdateHTMLParser
from unidown.plugins.mr_de.html_parser.list_html_parser import ListHTMLParser
from unidown.plugins.mr_de.html_parser.thread_html_parser import ThreadHTMLParser
from unidown.tools.tdqm_option import TdqmOption
from unidown.tools.tools import create_dir_rec, progress_bar


class Plugin(APlugin):
    """
    Pöugin class, derived from APlugin.
    """

    def __init__(self):
        super().__init__(PluginInfo('mr_de', '1.0.0', 'www.mobileread.com'))
        self.format_list = ['epub', 'mobi', 'lrf', 'imp', 'pdf', 'lit', 'azw', 'azw3', 'rar',
                            'lrx']  # TODO: make optional
        self.threads_path = self.temp_path.joinpath('threads/')
        self.unit = 'eBook'
        create_dir_rec(self.threads_path)

    def get_download_links(self):
        wiki_thread_dic = self.get_thread_links()  # link: name
        self.logging.info('Threads found: ' + str(len(wiki_thread_dic)))

        wiki_thread_dic = {k: wiki_thread_dic[k] for k in
                           list(wiki_thread_dic.keys())[:5]}  # DEV, just use five wiki threads

        self.download(wiki_thread_dic, self.threads_path, TdqmOption('Downloading threads', 'thread'))
        wiki_thread_dic, lost_dic = self.check_download(wiki_thread_dic, self.threads_path)
        if not wiki_thread_dic:
            raise GetDownloadLinksException("No thread was downloaded successful.")

        link_item_dict = self.get_ebook_links(wiki_thread_dic)
        return link_item_dict

    def get_last_update(self):
        self.logging.info('Download thread overview list')
        self.download_wiki_list()
        parser = LastUpdateHTMLParser()
        with self.temp_path.joinpath('main_list.html').open(mode='r', encoding="utf8") as reader:
            parser.feed(reader.read())
        if parser.wiki_list_date == datetime(1970, 1, 1):
            raise LastUpdateException("Something wents wrong with wikilist time.")
        return parser.wiki_list_date

    # -------------------------------------- #

    def get_thread_links(self):
        """
        Extract thread links from the wiki list.
        :return: dict[link, LinkItem]
        """
        thread_dic = {}
        for thread in self.extract_ebook_threads():  # add a download file name for every thread
            thread_dic[thread] = LinkItem(self.link_to_thread(thread), datetime(1970, 1, 1))
        return thread_dic

    @staticmethod
    def link_to_thread(link):
        """
        Convert link of a thread to a name which can be used as file name.
        :param link: link with special character
        :return: new link without special characters
        """
        return link.replace('?', '_').replace('/', '%') + '.html'

    def download_wiki_list(self):
        """
        Download the wiki list.
        """
        with urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where()) as https:
            with https.request('GET', 'https://wiki.mobileread.com/wiki/Free_eBooks-de/de', preload_content=False,
                               retries=urllib3.util.retry.Retry(3)) as load:
                with self.temp_path.joinpath('main_list.html').open(mode='wb') as out_file:
                    out_file.write(load.data)

    def extract_ebook_threads(self):
        """
        Extract the ebook threads from the wiki list.
        :return list with thread links
        """
        parser = ListHTMLParser(self.format_list)
        with self.temp_path.joinpath('main_list.html').open(mode='r', encoding="utf8") as reader:
            parser.feed(reader.read())
        parser.close()

        return parser.thread_list

    @staticmethod
    def get_ebook_links_from_file(path: Path):
        """
        Extract the ebook attachment links from given file.
        :return dict
        """
        try:
            parser = ThreadHTMLParser()
            with path.open(mode='r', encoding="utf-8", errors='ignore') as reader:
                parser.feed(reader.read())
            parser.close()
            link_item_dict = {}
            for item in parser.link_data_list:
                valid_name = re.sub(r'[^\w\-_. ]', '_', item[1])
                link_item_dict['/forums/attachment.php?attachmentid=' + item[0]] = LinkItem(valid_name, parser.time)
        except Exception:
            raise GetEbookLinksException(path, traceback.format_exc())
        if not link_item_dict:
            raise NothingFoundInThread(path)

        return link_item_dict

    def get_ebook_links(self, link_item_dict: dict):
        """
        Get all ebook links from the threads html with multi processing.
        :return dict[link, LinkItem]
        """
        job_list = []

        with ProcessPoolExecutor(max_workers=static_data.USING_CORES) as executor:
            for link, item in link_item_dict.items():  # all thread htmls
                path = self.threads_path.joinpath(item.name)
                job = executor.submit(self.get_ebook_links_from_file, path)
                job_list.append(job)

            pbar = progress_bar(job_list, TdqmOption('Extract ebook links', 'thread'))

        ebook_links = {}
        for job in job_list:  # merge all results into one dict
            try:
                result = job.result()
                for link in result.keys():  # no check if logging at warn level is chosen
                    if link in ebook_links:
                        self.logging.warning("Doubled link found: " + self.host + link)
                ebook_links.update(result)
            except NothingFoundInThread as ex:
                self.logging.info("Nothing found in " + str(ex.path))
            except GetEbookLinksException as ex:
                self.logging.error("Something went wrong in: " + str(ex.path) + ' | ' + ex.orig_ex)
                pbar.write('[Error] Something wents wrong. Please check the log file.')

        return ebook_links
