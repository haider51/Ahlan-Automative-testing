# pages/cart_page.py

from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

class CartPage(BasePage):
    # Locator: Check if our product is listed inside the cart
    CART_ITEM_TITLE = (AppiumBy.XPATH, "//*[@text='بجامة بأكمام واسعة']")

    # Action
    def is_product_in_cart(self):
        return self.is_element_visible(self.CART_ITEM_TITLE)