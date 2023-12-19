import pytest
from selene import browser, query


@pytest.fixture
def init_browser():
    browser.config.base_url = "https://demoqa.com"
    browser.config.window_width = 1280
    browser.config.window_height = 1024

    yield browser

    browser.quit()