import os

from common.common_utils.common_utils import CommonUtils

ELEMENT_WAIT_TIMEOUT = 10
ROOT_DIR = os.path.abspath(os.curdir)
UI_POLL_INTERVAL = 0.5
TIMEOUT = 10
SHORT_WAIT = 2000
TYPE_DELAY = 0.1
WAIT_TIME = 0.3
MAX_TRY_COUNT_API = 60
MAX_TRY_COUNT_UI = 30
ALLURE_PROPERTIES_FILE = CommonUtils.get_project_root() + "/allure-results/environment.properties"
RESOURCES_FOLDER = CommonUtils.get_project_root() + "/resources"
SCREENSHOTS_FOLDER = CommonUtils.get_project_root() + "/resources/screenshots"
VIDEOS_FOLDER = CommonUtils.get_project_root() + "/resources/videos"
SCREENSHOT_ON_SUCCESS = True
TIME_TO_DEPRECATE = 20
TIMESTAMP_FORMAT = "%m/%d/%Y-%H:%M:%S"
UI_TIME_FORMAT = "%Y-%m-%d"
