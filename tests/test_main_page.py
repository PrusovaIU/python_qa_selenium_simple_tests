from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


def test_content(browser):
    sleep(1)
    browser.find_element_by_id("content")


@pytest.mark.parametrize("locator",
                         [
                             pytest.param((By.NAME, "search"), id="Test_search"),
                             pytest.param((By.CLASS_NAME, "navbar-collapse"), id="Test menu"),
                             pytest.param((By.CSS_SELECTOR, ".col-lg-3"), id="Test goods cards")
                         ])
def test_find_elements(browser, locator: tuple):
    wait = WebDriverWait(browser, 3)
    wait.until(EC.visibility_of_element_located(locator))


def test_button(browser):
    cart = browser.find_element_by_id("cart")
    button = cart.find_element_by_class_name("btn")
    button.click()
    el: WebElement = WebDriverWait(browser, 3).until(
        lambda driver: driver.find_element_by_css_selector("#cart .dropdown-menu li p")
    )
    required_text = "Your shopping cart is empty!"
    assert el.text == required_text, f"Unexpected text: {el.text}. \"{required_text}\" is expected"

