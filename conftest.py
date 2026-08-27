# conftest.py

import pytest
import os
import re
from appium import webdriver
from appium.options.android import UiAutomator2Options
from utils.capabilities import get_android_capabilities
from utils.config import APPIUM_SERVER

@pytest.fixture(scope="function")
def mobile_driver(request):
    capabilities = get_android_capabilities()
    options = UiAutomator2Options().load_capabilities(capabilities)
    driver = webdriver.Remote(APPIUM_SERVER, options=options)

    # Attach driver to pytest node for screenshots on failure
    request.node.driver = driver

    yield driver

    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = getattr(item, "driver", None)
        if driver:
            os.makedirs("screenshots", exist_ok=True)
            safe_name = re.sub(r'[\\/*?:"<>| \-\[\]]', "_", item.name)
            screenshot_path = os.path.join("screenshots", f"{safe_name}.png")
            driver.get_screenshot_as_file(screenshot_path)
            print(f"\n[ALARM] Test failed! Screenshot saved to: {screenshot_path}")