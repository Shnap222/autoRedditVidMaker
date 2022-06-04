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
        self.page_interactor = PAGE_INTERACTOR(self.driver, 120)

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
        title_web_element.screenshot(screenshot_path.format(str(place)))
        place += 1

        texts.append(title_web_element.get_attribute("textContent"))

        for text_element in post_interactor.get_post_data():
            texts.append(text_element.get_attribute("textContent"))
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", text_element)
            text_element.screenshot(screenshot_path.format(str(place)))
            place += 1

        return output_dir_path, texts

    def _get_page(self, url: str = None):
        self.driver.get(url if url else self.url)

    # def get_images_and_voice(self,output_path:str=""):
    #     posts = []
    #     while not posts:
    #         self._get_page("https://www.reddit.com/")
    #         self._get_page()
    #         posts = self.page_interactor.get_posts()
    #
    #     for post in posts:
    #         tempdir, paragraphs = self._get_post_data(posts[1])
    #         audios_path = os.path.join(tempdir.name, 'audio')
    #         os.mkdir(audios_path)
    #         for num, paragraph in enumerate(paragraphs):
    #             self.audio_manager.record_text_to_file(path=os.path.join(audios_path, str(num)), text=paragraph)
    #
    #         final_video = os.path.join(tempdir.name, 'final.mp4')
    #
    #         half_made_videos_path = os.path.join(tempdir.name, 'half_made')
    #
    #         os.mkdir(half_made_videos_path)
    #
    #         self.movie_maker.create_movie_from_images_and_audios(audios_path=audios_path,
    #                                                              images_path=os.path.join(tempdir.name, 'images'),
    #                                                              output_path=half_made_videos_path)
    #
    #         self.movie_maker.create_video_with_background_video(
    #             bg_audio_path=r"C:\Users\smadar.KLAG\Downloads\LAKEY_INSPIRED_-_Better_Days_(getmp3.pro).mp3",
    #             bg_video_path=r'C:\Users\smadar.KLAG\Downloads\Free To Use Gameplay (No Copyright) - Minecraft Parkour.mp4',
    #             centered_videos_path=half_made_videos_path,
    #             output_path=r"C:\Users\smadar.KLAG\PycharmProjects\FilmEditor\FINAL.mp4"
    #         )
    #
    #         time.sleep(10000)

    # def _get_post_data(self, post):
    #     return self.page_interactor.extract_post_data(post)
