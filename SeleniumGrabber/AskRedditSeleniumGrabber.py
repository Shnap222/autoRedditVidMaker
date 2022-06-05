import os
import time
from typing import List, Tuple
import selenium.common.exceptions as ERRORS

from Abstract import IDataGatherer

from .grabber_config import *

from .SeleniumUtils import PageUtils

from Utils import FileUtilities


class AskRedditSeleniumGrabber(IDataGatherer.IDataGatherer):

    def __init__(self, posts_amount: int = 0):
        super().__init__(posts_amount)
        self.url = URL
        self.driver = PageUtils.create_driver_chrome(SERVICE_PATH)
        self.driver.set_window_size(width=849, height=1020)
        self.page_interactor = PAGE_INTERACTOR(self.driver, 20)
        self.comments_amount = 5

    def get_posts(self):

        posts = []

        # avoid rate limit
        while not posts:
            self._get_page("https://www.reddit.com/")
            self._get_page()
            posts = self.page_interactor.get_posts()
        return posts

    def get_post_data(self, post, output_dir_path: str) -> Tuple[str, List]:
        place = 0
        texts = []

        if output_dir_path:
            assert FileUtilities.check_dir_path(output_dir_path), "Non Existent Path"

        post_interactor = self.page_interactor.open_post(post)

        screenshot_path = os.path.join(output_dir_path, "{}.png")

        title_web_element = post_interactor.get_post_title()
        post_interactor.post_element.screenshot(screenshot_path.format(str(place)))
        place += 1

        texts.append(title_web_element.get_attribute("textContent"))

        comments = post_interactor.get_comments()

        limited_comments = comments if len(comments) <= self.comments_amount else comments[0:self.comments_amount]

        for comment_element in limited_comments:
            paragraph_elemets = comment_element.get_data()
            if not paragraph_elemets:
                continue
            # print(paragraph_elemets[0].get_attribute("textContent"))
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", paragraph_elemets[0])
            comment_text = []
            for paragraph in paragraph_elemets:
                comment_text.append(paragraph.get_attribute("textContent"))
            # todo fix the comment element XPATH needs to vote one div back
            # print(paragraph_elemets[-1].is_displayed())
            try:
                paragraph_elemets[-1].click()
            except ERRORS.ElementClickInterceptedException:
                continue
            texts.append(" ".join(comment_text))
            comment_element.screenshot(screenshot_path.format(str(place)))
            place += 1

        post_interactor.close_post_page()

        return output_dir_path, texts

    def _get_page(self, url: str = None):
        self.driver.get(url if url else self.url)
