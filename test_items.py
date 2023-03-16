import time
import math

from selenium.webdriver.common.by import By


def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    browser.implicitly_wait(3)
    find_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    assert find_button is not None

