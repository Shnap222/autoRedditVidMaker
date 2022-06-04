from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import selenium.common.exceptions as SELENIUM_ERROR
from selenium.webdriver.common.keys import Keys


def create_driver_chrome(service_path: str) -> webdriver.Chrome:
    ser = Service(service_path)
    op = webdriver.ChromeOptions()
    # op.add_argument('--start-maximized')
    return webdriver.Chrome(service=ser, options=op)

