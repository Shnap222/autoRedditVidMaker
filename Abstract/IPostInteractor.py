from abc import ABC, abstractmethod
import selenium.common.exceptions as ERRORS
from selenium.webdriver.common.by import By


class IPostInteractor(ABC):

    def __init__(self, driver, action, wait, post_element,font_size):
        self.driver = driver
        self.action = action
        self.wait = wait
        self.post_element = post_element
        self.font_size = font_size

    @abstractmethod
    def get_post_data(self):
        pass

    @abstractmethod
    def get_post_title(self):
        pass

    @abstractmethod
    def get_comments(self):
        pass

    @abstractmethod
    def close_post_page(self):
        pass

    def screen_shot_element(self, web_element, path):
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", web_element)
        web_element.screenshot(path)

    def zoom_element(self,web_element):
        self.driver.execute_script(f"arguments[0].style.zoom='{str(self.zoom_amount)}%';",web_element)