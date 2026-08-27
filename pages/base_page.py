# pages/base_page.py

import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def click_element(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def enter_text(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def is_element_visible(self, locator):
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            return element.is_displayed()
        except:
            return False

    def scroll_and_click(self, text):
        # 1. Scroll the element into view
        ui_scrollable = f'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().textContains("{text}"))'
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, ui_scrollable)
        
        # 2. Wait 1 second for scroll animation to completely stop
        time.sleep(1)
        
        # 3. Click the visible text or its parent card
        try:
            self.click_element((AppiumBy.XPATH, f"//*[@text='{text}']"))
        except:
            # Fallback: Click the card container wrapping the text
            self.click_element((AppiumBy.XPATH, f"//*[@text='{text}']/.."))