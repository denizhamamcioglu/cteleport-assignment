import logging

import playwright.sync_api
from playwright.sync_api import Page, Locator

from common import common_config


class AutomationUtils:
    def __init__(self, page: Page):
        self.page = page

    @staticmethod
    def optionally_wait_for_element(element: Locator, timeout: int = common_config.SHORT_WAIT):
        try:
            element.wait_for(state="attached", timeout=timeout)
        except playwright.sync_api.TimeoutError:
            pass

