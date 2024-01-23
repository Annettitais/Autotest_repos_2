from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pytest


@pytest.fixture()
def browser():
    options = Options()
    ##options.add_argument('--headless')
    ##options.add_argument('--no-sandbox')
    chrome_browser = webdriver.Chrome(options=options)
    return chrome_browser


def test_button_second(browser):
    browser.get('https://www.qa-practice.com/elements/button/simple')
    browser.find_element(By.ID, 'req_header').click()

