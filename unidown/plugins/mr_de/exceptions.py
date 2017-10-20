"""
mr_de specific module exceptions.
"""

from unidown.plugins.exceptions import ModuleException


class GetEbookLinksException(ModuleException):
    """
    Something wents wrong while parsing an wiki thread.
    """

    def __init__(self, path, orig_ex):
        super().__init__()
        self.path = path
        self.orig_ex = orig_ex


class NothingFoundInThread(ModuleException):
    """
    If no ebook in a wiki thread was found.
    """

    def __init__(self, path):
        super().__init__()
        self.path = path
