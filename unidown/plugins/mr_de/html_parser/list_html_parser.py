from html.parser import HTMLParser


class ListHTMLParser(HTMLParser):
    """
    Extractor for the forum threads of the wiki list.
    :ivar format_list: formats which should get
    :ivar last_link: last detected link
    :ivar thread_list: thread list
    """

    def __init__(self, format_list):
        """
        Constructor.
        :param format_list: which formats only should get
        """
        HTMLParser.__init__(self)
        self.format_list = format_list
        self.last_link = ''
        self.thread_list = []

    def error(self, message):
        raise Exception(message)

    def handle_starttag(self, tag, attrs):
        """
        Gets the last updated date of the wiki list and last possible thread link.
        """
        # a valid link must be inside of an 'a' tag
        if (tag != 'a') and (tag != 'span'):
            return
        for sub_tag, value in attrs:
            # if href is defined, set last_link
            if (sub_tag == "href") and (tag == 'a'):
                self.last_link = value

    def handle_endtag(self, tag):
        """
        Reset the last possible thread link if leaving the a tag.
        """
        # last_link is empty if outside of an 'a' tag
        if tag == 'a':
            self.last_link = ''

    def handle_data(self, data):
        """
        Check for legal thread link and append them.
        """
        # a valid link must be inside an 'a' tag and data must be a valid format
        # last_link is empty if outside of an 'a' tag
        if (data.lower() not in self.format_list) or (self.last_link == ''):
            return
        # cut the link, only the part after the hostname is needed
        self.last_link = self.last_link[25:]
        # only add unique links
        if self.last_link not in self.thread_list:
            self.thread_list.append(self.last_link)
