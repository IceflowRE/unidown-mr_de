"""
mr_de specific module exceptions.
"""
from pathlib import Path

from unidown.plugin.exceptions import PluginException


class GetEbookLinksException(PluginException):
    """
    Something wents wrong while parsing an wiki thread.
    Has default values due to python bug: https://bugs.python.org/issue37208
    """

    def __init__(self, path: Path = Path(''), orig_ex: Exception = None):
        super().__init__()
        self.path = path
        self.orig_ex = orig_ex


class NothingFoundInThread(PluginException):
    """
    If no ebook in a wiki thread was found.
    Has default values due to python bug: https://bugs.python.org/issue37208
    """

    def __init__(self, path: Path = Path('')):
        super().__init__()
        self.path = path
