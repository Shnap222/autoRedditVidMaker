from Abstract import ICommentInteractor

from selenium.webdriver.common.by import By


class RedditCommentInteractor(ICommentInteractor.ICommentInteractor):

    def __init__(self, web_element):
        super().__init__(web_element)

    def get_data(self):
        return self.web_element.find_element(By.XPATH, "//div[@data-testid='comment']/div/p").get_attribute(
            "textContent")
