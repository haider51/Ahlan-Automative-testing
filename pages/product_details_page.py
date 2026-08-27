# pages/product_details_page.py

from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

class ProductDetailsPage(BasePage):
    # Locators
    SIZE_M = (AppiumBy.XPATH, "//*[@text='M']")
    ADD_TO_CART_BUTTON = (AppiumBy.XPATH, "//*[@text='أضف إلى السلة']")
    BACK_BUTTON = (AppiumBy.XPATH, "//*[contains(@content-desc, 'Back') or @text='>' or @content-desc='Navigate up']")

    # Actions
    def select_size_m(self):
        self.click_element(self.SIZE_M)

    def click_add_to_cart(self):
        self.click_element(self.ADD_TO_CART_BUTTON)

    def go_back_to_home(self):
        try:
            self.click_element(self.BACK_BUTTON)
        except:
            # Fallback: Use Android native back navigation if the button has no text
            self.driver.back()