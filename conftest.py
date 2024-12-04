import logging
import os

import allure
import pytest
from dotenv import load_dotenv
from playwright.sync_api import Page
from pytest_bdd import given, parsers

from common import common_config
from common.common_utils.automation_utils import AutomationUtils
from pages.homepage.homepage_selectors import HomepageSelectors

load_dotenv()


@pytest.fixture(scope="function")
def page(request, browser) -> Page:
    os.makedirs(common_config.VIDEOS_FOLDER, exist_ok=True)
    base_url = os.getenv("TEST_URL", "https://www.kiwi.com/en/") or "https://www.kiwi.com/en/"
    context = browser.new_context(base_url=base_url, viewport={"width": 1920, "height": 1080},
                                  screen={"width": 1920, "height": 1080})
    page = context.new_page()
    yield page
    page.close()
    context.close()


@pytest.fixture(scope="session", autouse=True)
def set_playwright(playwright):
    playwright.selectors.set_test_id_attribute("data-test")


# common step definitions
@given(parsers.cfparse("As a {is_logged_in} user navigate to homepage"))
def navigate_to_homepage(page: Page, is_logged_in: str):
    page.goto("/")
    AutomationUtils(page).optionally_wait_for_element(HomepageSelectors(page).accept_cookies_button)

    if HomepageSelectors(page).accept_cookies_button:
        HomepageSelectors(page).accept_cookies_button.click()

    if "not" not in is_logged_in.lower():
        pass  # do the login operations if necessary.
