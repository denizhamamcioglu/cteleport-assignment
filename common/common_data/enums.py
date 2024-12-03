from enum import Enum


class RequestType(Enum):
    """
    Request Type enum class which contains the types of HTTP requests that are being used.
    """
    POST = "POST"
    GET = "GET"
    PUT = "PUT"
    DELETE = "DELETE"
    PATCH = "PATCH"
    OPTIONS = "OPTIONS"

    def __str__(self):
        """
        Returns the string instance of the desired enum key.
        Returns:
            String value of the desired enum key.

        """
        return str(self.value)

class TripType(Enum):
    """
    Trip Type enum class which contains the types of different trips supported by Kiwi.
    """
    ONE_WAY = "one-way"
    MULTI_CITY = "multi-city"
    NOMAD = "nomad"

    def __str__(self):
        """
        Returns the string instance of the desired enum key.
        Returns:
            String value of the desired enum key.

        """
        return str(self.value)
