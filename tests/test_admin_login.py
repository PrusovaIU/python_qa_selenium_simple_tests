from os.path import normpath
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def login(driver: WebDriver, user_name: str, password: str):
    input_name = driver.find_element_by_name("username")
    input_name.clear()
    input_name.send_keys(user_name)
    input_password = driver.find_element_by_name("password")
    input_password.clear()
    input_password.send_keys(password)
    button = driver.find_element_by_css_selector(".btn-primary")
    button.click()


def test_login_err(browser, admin):
    browser.get(normpath(f"{browser.current_url}/admin"))
    login(browser, admin[0], f"{admin[1]}1")
    wait = WebDriverWait(browser, 2)
    wait.until(EC.url_changes(f"{browser.current_url}/index.php?route=common/login"))
    alert: WebElement = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger")))
    alert_text = str(alert.text)
    assert alert_text.find("No match for Username and/or Password") != -1, \
        f"Unexpected alert:\n\t{alert_text}"


def test_login_suc(browser, admin):
    browser.get(normpath(f"{browser.current_url}/admin"))
    login(browser, admin[0], admin[1])
    wait = WebDriverWait(browser, 2)
    wait.until(EC.title_is("Dashboard"))


def test_forgot_password(browser):
    browser.get(normpath(f"{browser.current_url}/admin"))
    help_block = browser.find_element_by_css_selector(".help-block")
    a = help_block.find_element_by_tag_name("a")
    a.click()
    wait = WebDriverWait(browser, 2)
    wait.until(EC.title_contains("Forgot Your Password"))
    browser.find_element_by_name("email")
    text_right = browser.find_element_by_css_selector(".text-right")
    text_right.find_element_by_tag_name("button")
    text_right.find_element_by_tag_name("a")
