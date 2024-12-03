import logging
from typing import MutableMapping, Mapping, Any, Iterable, IO

import requests
import requests.adapters
from requests import Response, RequestException, Timeout, JSONDecodeError
from requests.cookies import RequestsCookieJar

from common import common_config

expected_status_codes = {
    "get": {200},
    "post": {200, 201, 204},
    "put": {200, 201, 204},
    "delete": {200, 204},
    "patch": {200},
    "head": {200, 201},
    "options": {200}
}


class RequestSender:
    """
    Sends an HTTP request with the given options.
    """

    @staticmethod
    def send_request(request_type: str, url: str, auth=None, query_parameters=None,
                     body: None | str | bytes | Mapping[str, Any] | Iterable[tuple[str, str | None]] | IO = None,
                     headers=None,
                     cookies: None | RequestsCookieJar | MutableMapping[str, str] = None,
                     auto_assert_response: bool = False) -> Response:
        """
        Sends an HTTP request with the given type, authentication, query parameters, body, headers and cookies to the given URL.
        Args:
            request_type (str): Type of the HTTP request. E.G: GET, POST, PUT, DELETE, etc.
            url (str): Target URL of the HTTP request.
            auth (tuple): Optional. Authentication for the HTTP request. None by default.
            query_parameters (dict): Optional. Query parameters of the HTTP request.
            body (object): Optional. Body of the HTTP request. None by default.
            headers (dict): Optional. Headers of the HTTP request. None by default.
            cookies (object): Optional. Cookies of the HTTP request. None by default.
            auto_assert_response (bool): If set to True, the received response code will automatically be asserted against the expected status codes for the provided request type. If set to False, auto verification step will be skipped. Check out expected_status_codes dictionary for the expected codes. False by default.

        Returns:
            Response: Response object of the sent HTTP request.
        """

        response = None
        session = requests.Session()
        adapter = requests.adapters.HTTPAdapter(max_retries=common_config.MAX_REQUEST_RETRY)
        session.mount("https://", adapter)

        logging.info(
            f"Core Process: Sending HTTP request with the following parameters: Request Type:{request_type} URL:{url} Auth:{auth} Query Parameters:{query_parameters} Body:{body} Headers:{headers} Cookies:{cookies} Verify Response:{auto_assert_response}")
        try:
            response = session.request(method=request_type, url=url, auth=auth, params=query_parameters, data=body,
                                       headers=headers, cookies=cookies, verify=False)
            logging.info(
                f"Core Process: HTTP request sent. Response Status: {response.status_code}. Response Body: {response.json()}")

        except Timeout as error:
            logging.error(f"Core Process: HTTP request resulted with a timeout. Error: {error}.")
        except RequestException as error:
            logging.error(f"Core Process: Request error while sending the HTTP request. Error: {error}.")
        except Exception as error:
            logging.info(f"Core Process: Unknown error while sending the HTTP request. Error: {error}.")

        finally:
            if auto_assert_response:
                logging.info(f"Core Process: Auto response assertion is set to true. Asserting the response.")
                try:
                    assert response.status_code in expected_status_codes[
                        request_type.lower()], f"Assertion: Response failed with status code: {response.status_code}\nResponse Body: {response.json()}"
                except JSONDecodeError:
                    assert response.status_code in expected_status_codes[
                        request_type.lower()], f"Assertion: Response failed with status code: {response.status_code}\nResponse Text: {response.text}"
                except AttributeError:
                    assert False, f"Assertion: Request failed without any response. Error message: {error}."

        return response
