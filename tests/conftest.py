import os

import pytest
from dotenv import load_dotenv
from selene import browser
from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from data import users_data
from pages.login_page import LoginPage
from utils import attach

DEFAULT_BROWSER_VERSION = "100.0"

login_page = LoginPage()
user = users_data.standard_user


def pytest_addoption(parser):
    parser.addoption(
        '--browser_version',
        default='100.0'
    )


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='session', autouse=True)
def set_browser(request):
    browser_version = request.config.getoption('--browser_version')
    browser_version = browser_version if browser_version != "" else DEFAULT_BROWSER_VERSION
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": browser_version,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)

    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')
    site = os.getenv('SITE')

    driver = webdriver.Remote(
        command_executor=f"https://{login}:{password}@{site}",
        options=options
    )

    browser.config.driver = driver

    browser.config.base_url = 'https://www.saucedemo.com'
    browser.config.timeout = 2
    browser.config.window_width = 1280
    browser.config.window_height = 1024

    yield browser

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()


@pytest.fixture(scope='function', autouse=True)
def open_browser(set_browser):
    browser.open('/')

    yield

    browser.open('/')


@pytest.fixture(scope='function', autouse=True)
def login_standard_user(open_browser):
    login_page.login(user)
