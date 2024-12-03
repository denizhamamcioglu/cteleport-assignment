from playwright.sync_api import Page


class HomepageSelectors:
    """
    Selectors for the homepage.
    """

    def __init__(self, page: Page):
        self.page = page

        # raw locator strings
        self.card_close_button_locator = "PlacePickerInputPlace-close"

        # buttons
        self.search_button = page.get_by_test_id("LandingSearchButton")
        self.accept_cookies_button = page.get_by_test_id("CookiesPopup-Accept")
        self.set_dates_button = page.get_by_test_id("SearchFormDoneButton")

        # divs
        self.one_way_trip_option = page.get_by_test_id("ModePopupOption-oneWay")
        self.multi_city_trip_option = page.get_by_test_id("ModePopupOption-multicity")
        self.nomad_trip_option = page.get_by_test_id("ModePopupOption-nomad")
        self.place_picker_city_row = page.get_by_test_id("PlacePickerRow-city")
        self.departure_div = page.get_by_test_id("PlacePickerInput-origin")
        self.destination_div = page.get_by_test_id("PlacePickerInput-destination")
        self.departure_date_div = page.get_by_test_id("SearchDateInput")

        # inputs

        # dropdowns
        self.trip_type_dropdown = page.locator("[data-test^='SearchFormModesPicker']")

        # checkboxes
        self.booking_checkbox = page.get_by_test_id("bookingCheckbox")

