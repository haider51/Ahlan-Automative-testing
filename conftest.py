import pytest
import os
import re
from appium import webdriver
from appium.options.common.base import AppiumOptions
from utils.capabilities import get_android_capabilities
# Assuming you have a config file, otherwise hardcode APPIUM_SERVER = "http://localhost:4723"
from utils.config import APPIUM_SERVER

@pytest.fixture(scope="function")
def mobile_driver(request):
    capabilities = get_android_capabilities()
    
    # We use base AppiumOptions for Flutter!
    options = AppiumOptions().load_capabilities(capabilities)
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
            import os, re
            os.makedirs("screenshots", exist_ok=True)
            safe_name = re.sub(r'[\\/*?:"<>| \-\[\]]', "_", item.name)
            screenshot_path = os.path.join("screenshots", f"{safe_name}.png")
            
            # THE FIX: Switch to Native Android just to snap the photo, then switch back!
            driver.switch_to.context('NATIVE_APP')
            driver.get_screenshot_as_file(screenshot_path)
            driver.switch_to.context('FLUTTER')
            
            print(f"\n[ALARM] Test failed! Screenshot saved to: {screenshot_path}")