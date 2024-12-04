# Deniz Hamamcioglu - CTeleport Take Home Assignment

## Features
The high-level features of this framework are:
1. Utilizes basic POM structure to separate the test logic and the page objects.
2. Contains many utility methods for random data generation, sending HTTP requests, automation helpers and many more.
3. Centralized configuration and data for page routes, environment information, configs.
4. Supports BDD.
5. Uses Playwright, Pytest.
6. Supports multi thread executions with xdist.
7. Contains Allure reports integration.
8. Contains basic GitHub Actions pipeline setup for CI executions.
9. Supports the retries of failed tests with different settings like delays and retry counts.

## Dependencies
1. **pytest**: Main test framework for assertions, fixtures, tagging, etc.
2. **requests**: Used for sending HTTP calls.
3. **allure-pytest**: Used for generating detailed HTML reports after test executions.
4. **Faker**: Used for generating meaningful random data such as names and email addresses.
5. **python-dotenv**: Used for reading key-value pairs from .env file and setting them as environment variables.
6. **pytest-rerunfailures**: Used for rerunning failed tests.
7. **pytest-xdist**: Used for parallel test executions.
8. **pytest-xdist[psutil]**: Used for utilizing the logical CPU cores (not just physical) for as well.
9. **playwright**: Test automation tool that we use for UI interactions.
10. **pytest-playwright**: Pytest adaptor of Playwright.
11. **pytest-bdd**: BDD support plugin for Pytest.

## Installation
To install the framework on your local machine, follow the steps described below:
1. Install Python 3.1x [Python Downloads Page](https://www.python.org/downloads/).
2. Execute `pip install -r requirements.txt` to install the automation framework dependencies.

## Executing the Tests
Pytest supports many ways to execute tests. In order to execute the tests with a specific marker (or tag), execute:
`pytest -m basic_search`

Available marker names can be checked from the pytest.ini file.

### Available Command Line Parameters
**-m**: Default pytest parameter. Used for specifying a test suite.<br>
Usage example: `pytest -m basic_search`

**--browser**: Browser to be used during the UI operations and UI tests.
Usage example: `pytest -k test_vanguard_link --browser chrome`

**--headed**: If provided, the tests will be executed in headed mode and a browser instance will be seen.
**dashboard-url**: URL of the dashboard application.

For default parameters of Playwright, check out [The official Playwright Documentation For Python](https://playwright.dev/docs/running-tests)

### Generating Test Reports
After each test, test results will be collected and saved to a folder called "allure-results". In order to compile the results and display it as a polished report, use the following command:
<br>`allure serve <path of the results directory>`

<br> If you encounter "Allure is not recognized as a command" error, install allure-commandline by using "npm install -g allure-commandline"

