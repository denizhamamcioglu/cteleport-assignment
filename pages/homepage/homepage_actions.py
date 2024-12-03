from playwright.sync_api import Page

from common.common_core.lazy_dictionary import LazyDictionary
from common.common_data.enums import TripType
from pages.homepage.homepage_selectors import HomepageSelectors


class HomepageActions:

    def __init__(self, page: Page):
        self.page = page
        self.homepage_selectors = HomepageSelectors(page=page)
        self.trip_type_selector_map = LazyDictionary({
            TripType.ONE_WAY.__str__(): (lambda x: self.homepage_selectors.one_way_trip_option, 0),
            TripType.MULTI_CITY.__str__(): (lambda x: self.homepage_selectors.multi_city_trip_option, 0),
            TripType.NOMAD.__str__(): (lambda x: self.homepage_selectors.nomad_trip_option, 0),
        })

    def select_departure(self, departure: str):
        self.homepage_selectors.departure_div.click()
        self.homepage_selectors.departure_div.locator("input").type(departure)
        self.homepage_selectors.place_picker_city_row.first.click()

    def select_destination(self, destination: str):
        self.homepage_selectors.destination_div.click()
        self.homepage_selectors.destination_div.locator("input").type(destination)
        self.homepage_selectors.place_picker_city_row.first.click()

    def select_trip_type(self, trip_type: str):
        self.homepage_selectors.trip_type_dropdown.click()
        self.trip_type_selector_map.get(trip_type).click()

    def enter_departure_date(self, departure_date: str):
        self.homepage_selectors.departure_date_div.click()
        self.page.locator(f"[data-value='{departure_date}']").click()
        self.homepage_selectors.set_dates_button.click()

    def toggle_check_booking_com_accommodation_checkbox(self, check: bool):
        if check:
            self.homepage_selectors.booking_checkbox.locator("input").check(force=True)
        else:
            self.homepage_selectors.booking_checkbox.locator("input").uncheck(force=True)