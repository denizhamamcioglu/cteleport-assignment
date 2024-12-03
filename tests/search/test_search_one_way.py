import re

from playwright.sync_api import Page, expect
from pytest_bdd import scenarios, given, when, then, parsers

from common import common_config
from common.common_data import environment
from common.common_utils.data_generator import DataGenerator
from pages.homepage.homepage_actions import HomepageActions
from pages.results.results_selectors import ResultsSelectors

scenarios("../../features/search")


@when(parsers.parse("Set the departure airport {departure}"))
def test_set_departure(departure: str, page: Page):
    HomepageActions(page).select_departure(departure)


@when(parsers.parse("Set the arrival airport {arrival}"))
def test_set_arrival(arrival: str, page: Page):
    HomepageActions(page).select_destination(arrival)


@when(parsers.cfparse("I select {trip_type} trip type"))
def test_select_trip_type(trip_type: str, page: Page):
    HomepageActions(page).select_trip_type(trip_type)


@when(parsers.cfparse("Set the departure time {delta_in_weeks} week(s) in the {tense} starting from current date"))
def test_select_trip_type(delta_in_weeks: str, tense: str, page: Page):
    if "future" in tense:
        date_to_enter = DataGenerator.get_delta_weeks_from_current_time(delta_in_weeks=int(delta_in_weeks),
                                                                        time_format=common_config.UI_TIME_FORMAT)
    else:
        date_to_enter = DataGenerator.get_delta_weeks_from_current_time(delta_in_weeks=-int(delta_in_weeks),
                                                                        time_format=common_config.UI_TIME_FORMAT)

    HomepageActions(page).enter_departure_date(date_to_enter)


@when(parsers.cfparse("{check} the 'Check accommodation with booking.com' option"))
def test_select_trip_type(check: str, page: Page):
    if "Uncheck" in check:
        HomepageActions(page).toggle_check_booking_com_accommodation_checkbox(check=False)
    else:
        HomepageActions(page).toggle_check_booking_com_accommodation_checkbox(check=True)


@when(parsers.cfparse("Click the search button"))
def test_select_trip_type(page: Page):
    HomepageActions(page).homepage_selectors.search_button.click()


@then(parsers.cfparse("I am redirected to the search results page"))
def test_select_trip_type(page: Page):
    expect(ResultsSelectors(page).quick_navigation_main_div, "Assertion: Quick navigation main div is not displayed after clicking the search button.").to_be_visible()

