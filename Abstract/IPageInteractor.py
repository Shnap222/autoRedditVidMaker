from typing import List
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from abc import ABC, abstractmethod


class IPageInteractor(ABC):

    def __init__(self, driver, font_size: int = 20):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.action = ActionChains(self.driver)
        self.font_size = font_size

    @abstractmethod
    def get_posts(self) -> List[object]:
        pass

    @abstractmethod
    def open_post(self, post) -> object:
        pass
