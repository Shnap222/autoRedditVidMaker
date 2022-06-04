from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium.common.exceptions as ERRORS


class RedditSettingsInteractor:

    def __init__(self, driver):
        self.driver = driver

    def click_user_dropdown(self):
        self.driver.find_element(By.ID, "USER_DROPDOWN_ID").click()

    def click_settings(self):
        self.driver.find_element(By.XPATH, "//span/span[text()[contains(., 'Settings')]]").click()

    def click_dark_mode(self):
        self.driver.find_element(By.XPATH, "//span[text()[contains(., 'Dark Mode')]]").click()
