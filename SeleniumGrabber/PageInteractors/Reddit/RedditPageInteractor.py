from typing import List
from selenium.webdriver.common.by import By

from SeleniumGrabber.PageInteractors.Reddit import RedditSettingsInteractor
from . import RedditPostInteractor
from Abstract import IPageInteractor


class RedditPageInteractor(IPageInteractor.IPageInteractor):

    def __init__(self, driver, zoom=0):
        super().__init__(driver, zoom)

        self.settings = RedditSettingsInteractor.RedditSettingsInteractor(self.driver)

    def get_posts(self) -> List[object]:
        self.zoom()
        return self.driver.find_elements(By.XPATH, "//div[contains(@class,'RichTextJSON-root')]")

    def open_post(self, post) -> RedditPostInteractor.RedditPostInteractor:
        post.click()
        return RedditPostInteractor.RedditPostInteractor(self.driver, self.action, self.wait)

# def extract_post_data(self, post) -> Tuple[tempfile.TemporaryDirectory, list]:
#     self.settings.click_user_dropdown()
#     self.settings.click_settings()
#     self.settings.click_dark_mode()
#
#     post.click()
#
#     text = []
#
#     tempdir = tempfile.TemporaryDirectory()
#     os.mkdir(os.path.join(tempdir.name, 'images'))
#     print(tempdir.name)
#
#     self.wait.until(EC.visibility_of_element_located(
#         (By.XPATH, "//div[@data-test-id='post-content']/div/div[contains(@class,'RichTextJSON-root')]/p")))
#
#     opened_post = self.driver.find_element(By.XPATH, "//div[@data-test-id='post-content']")
#
#     paragraphs = []
#
#     title = opened_post.find_element(By.XPATH, './div/div/div/h1')
#
#     paragraphs.append(title)
#
#     paragraphs += opened_post.find_elements(By.XPATH, "./div/div[contains(@class,'RichTextJSON-root')]/*")
#
#     for num, paragraph in enumerate(paragraphs):
#         self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", paragraph)
#         paragraph.screenshot(os.path.join(tempdir.name, "images", f"{num}.png"))
#         print(paragraph.get_attribute("textContent"))
#         text.append(paragraph.get_attribute('textContent'))
#
#     self._close_post_page()
#     print("finished")
#     return tempdir, text
