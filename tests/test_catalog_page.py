from os.path import normpath
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from typing import List


def test_goods_card(browser):
    browser.get(normpath(f"{browser.current_url}/desktops/mac"))
    wait = WebDriverWait(browser, 2)
    el: WebElement = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "col-lg-4")))
    el.find_element_by_class_name("button-group")


def test_cards_display(browser):
    browser.get(normpath(f"{browser.current_url}/desktops/mac"))
    wait = WebDriverWait(browser, 2)
    grid_button: WebElement = browser.find_element_by_id("grid-view")
    grid_button.click()
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "col-lg-4")))
    list_button: WebElement = browser.find_element_by_id("list-view")
    list_button.click()
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "col-xs-12")))


def test_sort(browser):
    browser.get(normpath(f"{browser.current_url}/desktops/mac"))
    el: WebElement = browser.find_element_by_id("input-sort")
    select = Select(el)
    select.select_by_visible_text("Name (A - Z)")
    WebDriverWait(browser, 1).until(EC.url_changes(f"{browser.current_url}/?sort=pd.name&order=ASC"))


def test_headbar(browser):
    browser.get(normpath(f"{browser.current_url}/desktops/mac"))
    els: List[WebElement] = browser.find_elements_by_css_selector(".breadcrumb")
    els_amount = len(els)
    assert els_amount == 1, f"Expected only one element with class name \"breadcrumb\", " \
                            f"but {els_amount} have been received"
    lis: List[WebElement] = els[0].find_elements_by_tag_name("li")
    lis_amount = len(lis)
    assert lis_amount == 3, f"Expected 3 elements li, but {lis_amount} have been received"


def test_compare(browser):
    browser.get(normpath(f"{browser.current_url}/desktops/mac"))
    required_id = "compare-total"
    els: List[WebElement] = browser.find_elements_by_id(required_id)
    assert len(els) == 1, f"There are few elements with id \"{required_id}\""
