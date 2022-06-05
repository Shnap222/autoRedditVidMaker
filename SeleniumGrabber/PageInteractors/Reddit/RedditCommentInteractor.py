from Abstract import ICommentInteractor

from selenium.webdriver.common.by import By


class RedditCommentInteractor(ICommentInteractor.ICommentInteractor):

    def __init__(self, web_element, driver, font_size: int = 20):
        super().__init__(web_element, driver, font_size)

    def get_data(self):
        texts = self.web_element.find_elements(By.XPATH, "./div/div[@data-testid='comment']/div/p")

        for element in texts:
            self.driver.execute_script(f"arguments[0].setAttribute('style','font-size : {self.font_size}px ;')",
                                       element)

        return texts
