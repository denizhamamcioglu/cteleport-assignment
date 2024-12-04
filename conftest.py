import logging
import os

import allure
import pytest
from _pytest.nodes import Item
from _pytest.runner import CallInfo
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
    context = browser.new_context(base_url=base_url, viewport={"width": 1920, "height": 1080}, record_video_dir="./resources/videos")
    page = context.new_page()
    yield page
    page.close()
    context.close()


@pytest.fixture(scope="session", autouse=True)
def set_playwright(playwright):
    playwright.selectors.set_test_id_attribute("data-test")


def attach_screenshot_to_test_report(page: Page, name: str = "screenshot"):
    logging.info(f"Core Process (fixture): Capturing a screenshot.")
    screenshot = page.screenshot(full_page=True)
    logging.info(f"Core Process (fixture): Attaching the screenshot to the Allure report.")
    allure.attach(screenshot, name=name, attachment_type=allure.attachment_type.PNG)


def attach_video_to_test_report(page: Page, name: str = "video"):
    logging.info(f"Core Process (fixture): Getting the video recording of the failed test.")
    video_path = page.video.path()
    page.context.close()
    with open(video_path, "rb") as video_file:
        logging.info(f"Core Process (fixture): Attaching the test video to the Allure report.")
        allure.attach(video_file.read(), name=name, attachment_type=allure.attachment_type.WEBM)


# common step definitions
@given(parsers.cfparse("As a {is_logged_in} user navigate to homepage"))
def navigate_to_homepage(page: Page, is_logged_in: str):
    page.goto("/")
    AutomationUtils(page).optionally_wait_for_element(HomepageSelectors(page).accept_cookies_button)

    if HomepageSelectors(page).accept_cookies_button.is_visible():
        HomepageSelectors(page).accept_cookies_button.click()

    if "not" not in is_logged_in.lower():
        pass  # do the login operations if necessary.


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item: Item, call: CallInfo[None]):
    outcome = yield
    result = outcome.get_result()

    if hasattr(item.config, "workerinput"):
        if result.when == "call" or result.when == "setup":
            if result.when == "call" and result.failed:
                try:
                    page: Page = item.funcargs["page"]
                    attach_screenshot_to_test_report(page=page)
                    attach_video_to_test_report(page=page)

                except KeyError:
                    logging.info(
                        f"Core Process (fixture): No page instance exists to take a screenshot.")

            logging.info(
                f"Core Process (Test Level): Test is being executed inside a thread (xdist node). Collecting test metadata.")

        logging.info(
            f"Core Process (Test Level): Test metadata collection from {item.config.workerinput['workerid']} is done.")
