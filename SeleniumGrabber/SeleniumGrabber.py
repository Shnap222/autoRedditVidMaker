import os
import time
from typing import List, Tuple

from Abstract import IDataGatherer

from .grabber_config import *

from .SeleniumUtils import PageUtils

from Utils import FileUtilities


class SeleniumGraber(IDataGatherer.IDataGatherer):

    def __init__(self, posts_amount: int = 0):
        super().__init__(posts_amount)
        self.url = URL
        self.driver = PageUtils.create_driver_chrome(SERVICE_PATH)
        self.driver.set_window_size(width=849, height=1020)
        self.page_interactor = PAGE_INTERACTOR(self.driver, 20)

    def get_posts(self):

        posts = []

        # avoid rate limit
        while not posts:
            self._get_page("https://www.reddit.com/")
            self._get_page()
            posts = self.page_interactor.get_posts()

        posts.pop(0)

        return posts

    def get_post_data(self, post, output_dir_path: str) -> Tuple[str, List]:
        place = 0
        texts = []

        if output_dir_path:
            assert FileUtilities.check_dir_path(output_dir_path), "Non Existent Path"

        post_interactor = self.page_interactor.open_post(post)

        screenshot_path = os.path.join(output_dir_path, "{}.png")

        title_web_element = post_interactor.get_post_title()
        title_web_element.screenshot(screenshot_path.format(str(place)))
        place += 1

        texts.append(title_web_element.get_attribute("textContent"))

        for text_element in post_interactor.get_post_data():
            texts.append(text_element.get_attribute("textContent"))
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", text_element)
            text_element.screenshot(screenshot_path.format(str(place)))
            place += 1

        post_interactor.close_post_page()


        return output_dir_path, texts

    def _get_page(self, url: str = None):
        self.driver.get(url if url else self.url)
