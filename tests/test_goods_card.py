from os.path import normpath
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from typing import List
import pytest


def test_add_to_cart(browser):
    browser.get(normpath(f"{browser.current_url}/desktops/mac/imac"))
    wait = WebDriverWait(browser, 2)
    button_add: WebElement = wait.until(EC.visibility_of_element_located((By.ID, "button-cart")))
    button_add.click()
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert-success")))
    cart = browser.find_element(value="cart")
    button_cart = cart.find_element_by_tag_name("button")
    button_cart.click()
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#cart .dropdown-menu")))


@pytest.mark.parametrize("locator",
                         [
                             pytest.param((By.CLASS_NAME, "col-sm-8"), id="By_class_name"),
                             pytest.param((By.CSS_SELECTOR, ".col-sm-4"), id="By css selector")
                         ])
def test_element_is_present(browser, locator):
    browser.get(normpath(f"{browser.current_url}/desktops/mac/imac"))
    wait = WebDriverWait(browser, 2)
    wait.until(EC.visibility_of_element_located(locator))


def test_images(browser):
    browser.get(normpath(f"{browser.current_url}/desktops/mac/imac"))
    wait = WebDriverWait(browser, 2)
    image_list: WebElement = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".thumbnails")))
    lis: List[WebElement] = image_list.find_elements_by_tag_name("li")
    for li in lis:
        a: WebElement = li.find_element_by_tag_name("a")
        a.click()
        image_content: WebElement = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".mfp-content")))
        button_close = image_content.find_element_by_tag_name("button")
        button_close.click()


def test_move(browser):
    browser.get(normpath(f"{browser.current_url}/desktops/mac/imac"))
    wait = WebDriverWait(browser, 2)
    share: WebElement = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "a.atc_s.addthis_button_compact")))
    ActionChains(browser).move_to_element(share).perform()
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#at15s")))
