from playwright.sync_api import Page


class ResultsSelectors:
    """
    Selectors for the results page.
    """

    def __init__(self, page: Page):
        self.page = page

        # raw locator strings

        # buttons

        # divs
        self.quick_navigation_main_div = page.get_by_test_id("QuickNavigationSection")

        # inputs

        # dropdowns

        # checkboxes

