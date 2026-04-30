
import os
import time
from datetime import datetime

import pytest
import self
from selenium import webdriver

from utilities import ScreenshotUtility


@pytest.fixture
def browserinstance():
    driver = webdriver.Chrome()  # or Firefox(), Edge(), etc.
    driver.get("https://groceryapp.uniqassosiates.com/admin/login")
    time.sleep(5)
    driver.maximize_window()
    yield driver
    """driver.get("https://groceryapp.uniqassosiates.com/admin/login")
    time.sleep(5)
    driver.maximize_window()
    time.sleep(3)"""


@pytest.fixture(params=["chrome","firefox","edge"])
def crossbrowser(request):

    browser_name = request.param
    if browser_name=="chrome":
        driver = webdriver.Chrome()
    elif browser_name=="firefox":
        driver = webdriver.Firefox()
    elif browser_name=="edge":
        driver = webdriver.Edge()

    driver.implicitly_wait(10)
    yield driver


REPORT_FOLDER = None

def pytest_configure(config):
    global REPORT_FOLDER
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    REPORT_FOLDER = os.path.abspath(os.path.join(os.path.dirname(__file__), 'reports', timestamp))
    os.makedirs(REPORT_FOLDER, exist_ok=True)
    # Override the HTML report output path dynamically
    config.option.htmlpath = os.path.join(REPORT_FOLDER, "report.html")

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    global REPORT_FOLDER
    pytest_html = item.config.pluginmanager.getplugin('html')

    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extras', [])

    if report.when in ('setup', 'call'):
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            safe_name = report.nodeid.replace("::", "_").replace("/", "_")
            screenshot_path = os.path.join(REPORT_FOLDER, f"{safe_name}.png")
            print(f"Capturing screenshot: {screenshot_path}")

            ScreenshotUtility.capture_screenshot(item, screenshot_path)

            if os.path.exists(screenshot_path):
                html = (
                    f'<div><img src="file://{screenshot_path}" alt="screenshot" '
                    'style="width:304px;height:228px;" onclick="window.open(this.src)" align="right"/></div>'
                )
                extra.append(pytest_html.extras.html(html))

        report.extras = extra