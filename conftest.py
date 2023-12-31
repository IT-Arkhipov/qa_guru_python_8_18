import pytest

from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def init_browser():

    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor=f"https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options
    )

    browser.config.driver = driver
    browser.config.base_url = "https://demoqa.com"
    browser.config.window_width = 1280
    browser.config.window_height = 1024

    yield browser

    browser.quit()