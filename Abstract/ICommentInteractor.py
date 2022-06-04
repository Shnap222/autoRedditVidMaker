from abc import ABC, abstractmethod


class ICommentInteractor(ABC):

    def __init__(self, web_element):
        self.web_element = web_element

    @abstractmethod
    def get_data(self):
        pass

    def screenshot(self, path):
        self.web_element.screenshot(path)
