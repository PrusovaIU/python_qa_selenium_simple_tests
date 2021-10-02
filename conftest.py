from os.path import expanduser
from selenium import webdriver
from typing import Tuple
import pytest


BROWSER = "--browser"
URL = "--url"
DRIVERS = "--drivers"
HEADLESS = "--headless"
ADMIN_NAME = "--user"
ADMIN_PASSWORD = "--password"


def pytest_addoption(parser):
    parser.addoption(BROWSER, action="store", default="chrome")
    parser.addoption(URL, action="store", default="https://demo.opencart.com/")
    parser.addoption(DRIVERS, action="store", default=expanduser("~/Downloads/drivers"))
    parser.addoption(HEADLESS, action="store_true")
    parser.addoption(ADMIN_NAME, action="store", default="user")
    parser.addoption(ADMIN_PASSWORD, action="store", default="bitnami")


@pytest.fixture
def browser(request):
    browser = request.config.getoption(BROWSER)
    url = request.config.getoption(URL)
    drivers = request.config.getoption(DRIVERS)
    headless = request.config.getoption(HEADLESS)

    def add_options(options_type):
        options = options_type()
        options.headless = headless
        return options

    if browser == "chrome":
        driver = webdriver.Chrome(executable_path=drivers + "/chromedriver",
                                  options=add_options(webdriver.ChromeOptions))
    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path=drivers + "/geckodriver",
                                   options=add_options(webdriver.FirefoxOptions))
    elif browser == "opera":
        driver = webdriver.Opera(executable_path=drivers + "/operadriver")
    else:
        raise Exception("Unknown browser")

    driver.maximize_window()

    request.addfinalizer(driver.close)

    driver.get(url)
    driver.url = url

    return driver


@pytest.fixture
def admin(request) -> Tuple[str, str]:
    name = request.config.getoption(ADMIN_NAME)
    password = request.config.getoption(ADMIN_PASSWORD)
    return name, password
