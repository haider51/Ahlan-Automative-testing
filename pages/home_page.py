# pages/home_page.py

from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

class HomePage(BasePage):
    # Locators
    NAV_CART_BUTTON = (AppiumBy.XPATH, "//*[@text='سلة التسوق']")

    # Actions
    def select_pajama_product(self):
        # Automatically scrolls down until it finds the pajama and clicks it!
        self.scroll_and_click("بجامة بأكمام واسعة")

    def open_cart_from_bottom_nav(self):
        self.click_element(self.NAV_CART_BUTTON)