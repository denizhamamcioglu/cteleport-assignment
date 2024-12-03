import logging
import math
import random
import string
import datetime
from faker import Faker

from common import common_config


class DataGenerator:
    """
    Generates random data.
    """
    @staticmethod
    def generate_random_string(length: int, prefix: str = "") -> str:
        """
        Generates a random string with the given length and optional prefix.
        Args:
            length (int): Length of the random string that will be generated.
            prefix (str): Optional. Prefix that will be prepended to the random string.

        Returns:
            (str): Random string with the given length and prefix.
        """
        random_string = prefix + ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        logging.info(f"Core Process: Generated a random string: {random_string}.")
        return random_string

    @staticmethod
    def generate_random_number(length: int) -> int:
        """
        Generates random number with the given length.
        Args:
            length (int): Length of the random number that will be generated.

        Returns:
            (int): Random number with the given length.
        """
        random_number = int(''.join(random.choices(string.digits, k=length)))
        logging.info(f"Core Process: Generated a random number: {random_number}")
        return random_number

    @staticmethod
    def generate_random_number_between(minimum: int, maximum: int) -> int:
        """
        Generates a random number between the given minimum and maximum range.
        Args:
            minimum (int): Minimum range of the random number.
            maximum (int): Maximum range of the random number.

        Returns:
            (int) Random number within the given range.
        """
        random_number = random.randrange(minimum, maximum, 3)
        logging.info(f"Core Process: Generated a random number between {minimum} and {maximum}. Number is: {random_number}.")
        return random_number

    @staticmethod
    def generate_random_email(length: int, prefix: str = "") -> str:
        """
        Generates a random email with the given length and prefix. Uses generate_random_string().
        Args:
            length (int): Length of the random email that will be generated.
            prefix (str): Optional. Prefix that will be prepended to the random string.

        Returns:
            (str): Random email address with the given length and prefix.

        """
        random_email = DataGenerator.generate_random_string(length, prefix) + "@fakemail.com"
        logging.info(f"Core Process: Generated a random email: {random_email}")
        return random_email

    @staticmethod
    def generate_random_name(locale: str) -> str:
        """
        Generates a random future date between 1 day from now and the given end date, with the given time format.
        Args:
            locale (str): Origin of the name.

        Returns:
            (str): Random name with the given locale.
        """
        random_name = Faker(locale).name()
        logging.info(f"Core Process: Generated a random name with locale: {locale}. Name: {random_name}.")
        return random_name

    @staticmethod
    def generate_random_future_date(end_date: str = None, time_format: str = None) -> str:
        """
        Generates a random future date between 1 day from now and the given end date, with the given time format.
        Args:
            end_date (str): Future end date of the random date. Examples: +30y (30 years from now), +10d (10 days from now).
            time_format (str): Date time format of the generated date. Example: "%m/%d/%Y, %H:%M:%S"

        Returns:
            (str): Random future date in the datetime format.

        """
        random_future_date = Faker().future_datetime(end_date).strftime(time_format)

        logging.info(f"Core Process: Generated a random future date before {end_date}. Date is: {random_future_date}.")
        if time_format == common_config.UI_TIME_FORMAT:
            return random_future_date.replace(" 0", " ")

        return random_future_date

    @staticmethod
    def generate_random_past_date(start_date: str = None, time_format: str = None) -> str:
        """
        Generates a random past date between 1 second before now and the given start date.
        Args:
            start_date (str): Future end date of the random date. Examples: -30y (30 years ago), -10d (10 days ago).
            time_format (str): Date time format of the generated date. Example: "%m/%d/%Y, %H:%M:%S"

        Returns:
            (str): Random past date in the datetime format.

        """
        random_past_date = Faker().past_datetime(start_date).strftime(time_format)
        logging.info(f"Core Process: Generated a random past date after {start_date}. Date is: {random_past_date}.")
        return random_past_date

    @staticmethod
    def generate_random_dates_between(start_date: str, end_date: str, time_format: str) -> str:
        """
        Generates a random date between the given start_date and end_date timeframes.
        Args:
            start_date (str): Start past date of the random date. Examples: -30y (30 years ago), -10d (10 days ago).
            end_date (str): Future end date of the random date. Examples: +30y (30 years from now), +10d (10 days from now).
            time_format (str): Date time format of the generated date. Example: "%m/%d/%Y, %H:%M:%S"

        Returns:
            (str): Random date in the datetime format.
        """
        random_date = Faker().date_time_between(start_date, end_date).strftime(time_format)
        logging.info(f"Core Process: Generated a random number between {start_date} and {end_date}. Date is: {random_date}.")
        return random_date

    @staticmethod
    def generate_timestamp() -> float:
        """
        Generates a conventional timestamp.
        Returns:
            (float): Current timestamp in milliseconds.
        """
        timestamp = datetime.datetime.timestamp()
        logging.info(f"Core Process: Generated a timestamp: {timestamp}.")
        return timestamp

    @staticmethod
    def generate_readable_timestamp() -> datetime:
        """
        Generates a meaningful - human-readable timestamp.
        Returns:
            (datetime): Timestamp in %Y-%m-%d %H-%M-%S.%s format.

        """
        meaningful_timestamp = datetime.datetime.now()
        logging.info(f"Core Process: Generated meaningful timestamp: {str(meaningful_timestamp)}.")
        return meaningful_timestamp

    @staticmethod
    def get_current_time(time_format: str) -> str:
        """
        Returns the current time in the given format.
        Args:
            time_format (str): Desired format of the returned date/time.

        Returns:
            (datetime): Current time in the given format. Example: %m/%d/%Y, %H:%M:%S

        """
        current_time = datetime.datetime.now().strftime(time_format)
        logging.info(f"Core Process: Getting the current time: {current_time}.")
        return current_time

    @staticmethod
    def get_delta_minutes_from_current_time(time_format: str, delta_in_minutes: int) -> str:
        """
        Returns the given amount of delta minutes from the current time.
        Args:
            time_format (str): Desired format of the returned date/time. Example: %m/%d/%Y, %H:%M:%S
            delta_in_minutes (int): Delta minute value that will be added or subtracted from the current time.

        Returns:
            (str): The given amount of delta minutes from the current time.

        """
        time_delta = (datetime.datetime.now() + datetime.timedelta(minutes=delta_in_minutes)).strftime(time_format)
        logging.info(f"Core Process: Getting the {delta_in_minutes} minutes of delta from the current time. Result is: {time_delta}.")
        return time_delta

    @staticmethod
    def get_delta_days_from_current_time(time_format: str, delta_in_days: int) -> str:
        """
        Returns the given amount of delta days from the current time.
        Args:
            time_format (str): Desired format of the returned date/time. Example: %m/%d/%Y, %H:%M:%S
            delta_in_days (int): Delta day value that will be added or subtracted from the current time.

        Returns:
            (str): The given amount of delta days from the current time.

        """
        time_delta = (datetime.datetime.now() + datetime.timedelta(days=delta_in_days)).strftime(time_format)
        logging.info(
            f"Core Process: Getting the {delta_in_days} minutes of delta from the current time. Result is: {time_delta}.")
        return time_delta

    @staticmethod
    def get_delta_weeks_from_current_time(delta_in_weeks: int, time_format: str) -> str:
        """
        Returns the given amount of delta weeks from the current time.
        Args:
            delta_in_weeks (int): Delta week value that will be added or subtracted from the current time.
            time_format (str): Desired format of the returned date/time. Example: %m/%d/%Y, %H:%M:%S

        Returns:
            (str): The given amount of delta weeks from the current time.

        """
        time_delta = (datetime.datetime.now() + datetime.timedelta(weeks=delta_in_weeks)).strftime(time_format)
        logging.info(
            f"Core Process: Getting the {delta_in_weeks} minutes of delta from the current time. Result is: {time_delta}.")
        return time_delta

    @staticmethod
    def get_delta_seconds_from_current_time(time_format: str, delta_in_seconds: int) -> str:
        """
        Returns the given amount of delta seconds from the current time.
        Args:
            time_format (str): Desired format of the returned date/time. Example: %m/%d/%Y, %H:%M:%S
            delta_in_seconds (int): Delta second value that will be added or subtracted from the current time.

        Returns:
            (str): The given amount of delta seconds from the current time.

        """

        time_delta = (datetime.datetime.now() + datetime.timedelta(seconds=delta_in_seconds)).strftime(time_format)
        logging.info(f"Core Process: Getting the {delta_in_seconds} seconds of delta from the current time. Result is: {time_delta}.")
        return time_delta

    @staticmethod
    def get_timestamp_delta_seconds_from_current_time(delta_in_seconds: int) -> int:
        """
        Returns a timestamp with the given amount of delta seconds from the current time.
        Args:
            delta_in_seconds (int): Delta second value that will be added or subtracted from the current time.

        Returns:
            (int): Timestamp with the given amount of delta seconds from the current time.

        """

        timestamp_delta = math.floor((datetime.datetime.now() + datetime.timedelta(seconds=delta_in_seconds)).timestamp())
        logging.info(f"Core Process: Getting the {delta_in_seconds} delta from the current timestamp. Value is: {timestamp_delta}.")
        return timestamp_delta
