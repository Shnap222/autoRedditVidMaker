from abc import ABC, abstractmethod


class ICommentInteractor(ABC):

    def __init__(self, web_element, driver, font_size: int = 20):
        self.web_element = web_element
        self.driver = driver
        self.font_size = font_size

    @abstractmethod
    def get_data(self):
        pass

    def screenshot(self, path):
        self.web_element.screenshot(path)
