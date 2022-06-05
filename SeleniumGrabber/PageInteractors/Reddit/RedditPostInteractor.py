from Abstract import IPostInteractor
import selenium.common.exceptions as ERRORS
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from . import RedditCommentInteractor


class RedditPostInteractor(IPostInteractor.IPostInteractor):

    def __init__(self, driver, action, wait, post_element=None, font_size: int = 20):

        try:
            wait.until(EC.visibility_of_element_located(
                (By.XPATH, "//div[@data-test-id='post-content']/div/div[contains(@class,'RichTextJSON-root')]/p")))
        except ERRORS.TimeoutException:
            wait.until(EC.visibility_of_element_located((By.XPATH,"//div[@data-test-id='post-content']")))

        if not post_element:
            post_element = driver.find_element(By.XPATH, "//div[@data-test-id='post-content']")

        super().__init__(driver, action, wait, post_element, font_size)

        # self.zoom_element(post_element)
        self.post_element = driver.find_element(By.XPATH, "//div[@data-test-id='post-content']")
        self.memo = {}

    def get_post_title(self):
        title = self.post_element.find_element(By.XPATH, './div/div/div/h1') if "title" not in self.memo.keys() else \
            self.memo['title']
        self._update_memo('title', title)
        return title

    def get_post_data(self) -> list:
        data = self.post_element.find_elements(By.XPATH,
                                               "./div/div[contains(@class,'RichTextJSON-root')]/*") if "data" not in self.memo.keys() else \
            self.memo['data']
        self._update_memo('data', data)
        for element in data:
            self.driver.execute_script(f"arguments[0].setAttribute('style','font-size : {self.font_size}px ;')", element)
        return data

    def get_comments(self):
        return [RedditCommentInteractor.RedditCommentInteractor(comment,self.driver,self.font_size) for comment in
                self.driver.find_elements(By.XPATH,'//div[contains(@class,"Comment")]/div/span[contains(text(),"level 1")]/../..')]

    def close_post_page(self):
        current_url = self.driver.current_url

        while current_url == self.driver.current_url:

            try:
                self.driver.find_element(By.XPATH, "//button[@title='Close']").click()
            except ERRORS.ElementClickInterceptedException as e:
                self.driver.execute_script("""
                  var b = document.querySelectorAll("[role=dialog]");
                  b=b[0].parentElement;
                  b.parentElement.removeChild(b);
                  """)

    def _update_memo(self, key, value):
        if key in self.memo.keys():
            return
        self.memo[key] = value
