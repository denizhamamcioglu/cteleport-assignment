import datetime
import logging
import os
import time

import pytest

from common.common_data.enums import RequestType
from common import common_config
from common.common_utils.data_generator import DataGenerator


class CommonUtils:
    """
    Common utility class which contains helper methods that can be used across the project.
    """

    @staticmethod
    def is_app_running_in_github_actions() -> bool:
        """
        Checks if the tests are being executed inside GitHub Actions environment.
        Returns:
            result (bool): True if the app is running in a GitHub Actions environment, False otherwise.

        """

        logging.info(f"Core Process: Checking if the tests are running inside the GitHub Actions environment.")
        result = "GITHUB_ACTIONS" in os.environ and os.environ["GITHUB_ACTIONS"] == "true"
        logging.info(f"Core Process: Is the app running inside the GitHub Actions environment: {result}.")
        return result

    @staticmethod
    def is_app_running_inside_docker() -> bool:
        """
        Checks if the app is running inside a Docker container.
        Returns:
            result (bool): True if the app is running inside a Docker container. False otherwise.

        """

        logging.info(f"Core Process: Checking if the app is running inside a Docker container.")
        path = "/proc/self/cgroup"
        result = os.path.exists("/.dockerenv") or os.path.isfile(path) and any("docker" in line for line in open(path))
        logging.info(f"Core Process: Is the app running inside a Docker container: {result}.")
        return result

    @staticmethod
    def get_project_root():
        """
        Returns the root path of the project.
        Returns:
            (str): Root path of the project.

        """

        logging.info(f"Core Process: Returning the root path of the project.")
        return common_config.ROOT_DIR.split("cteleport-assignment")[0] + "cteleport-assignment"

    @staticmethod
    def pause_until(target_time: str, time_format: str):
        """
        Pauses the code execution until the given target time has been reached.
        Args:
            target_time (str): Target time until the code execution will be paused.
            time_format (str): Format of the target time

        Returns:
            None.
        """

        current_time = DataGenerator.generate_readable_timestamp()
        target = datetime.datetime.strptime(target_time, time_format)
        delta = target - current_time

        logging.debug(f"Core Process: Current time: {current_time}. Target time: {target}. Delta: {delta}.")

        if delta > datetime.timedelta(minutes=0):
            logging.info(f"Core Process: Pausing the code execution until: {target}")
            time.sleep(delta.total_seconds())

    @staticmethod
    def pause(amount: int):
        """
        Pauses the code execution for the given amount.
        Args:
            amount (int): Amount to pause in seconds.

        Returns:
            None.

        """
        logging.info(f"Core Process: Pausing for {amount} seconds.")
        time.sleep(amount)

    @staticmethod
    def get_time_difference(start_date: str, end_date: str, time_format: str) -> int:
        """
        Calculates the difference between two dates, according to the given format.
        Args:
            start_date (str): The start date.
            end_date (str): The end date.
            time_format (str): Format of the target time.

        Returns:
            result (int): Difference between the given two dates.
        """

        start_date_formatted = datetime.datetime.strptime(start_date, time_format)
        end_date_formatted = datetime.datetime.strptime(end_date, time_format)

        result = int((end_date_formatted - start_date_formatted).days)
        logging.info(f"Core Process: Calculated the time difference between {end_date} and {start_date}. Result is {result}")
        return result

    @staticmethod
    def get_current_geo_location() -> str:
        """
        Returns the current GEO location of the host machine that executes the tests.
        Returns:
            result (str): Current location.
        """
        from common.common_utils.request_sender import RequestSender
        result = RequestSender.send_request(request_type=RequestType.GET.__str__(),
                                            url="https://ipinfo.io/json").json()["country"]

        logging.info(f"Core Process: Fetched the current GEO location. Current location is {result}.")
        pytest.current_geo_location = result
        return result

    @staticmethod
    def search_dictionary_for_keyword(dictionary: dict, keyword: str) -> list:
        """
        Searches the given dictionary for the given keyword.
        Args:
            dictionary (dict): Dictionary to be searched for.
            keyword: keyword to search inside the dictionary items.

        Returns (list): List of results.

        """
        result = []
        logging.info(f"Core Process: Searching {keyword} in dictionary.")

        for key, value in dictionary.items():
            for item in value:
                if keyword in item.__str__():
                    result.append(item)

        return result
