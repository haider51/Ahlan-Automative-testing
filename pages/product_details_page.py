from pages.base_page import BasePage, finder

class ProductDetailsPage(BasePage):
    # Tell developers to add these keys to the App!
    SIZE_M = finder.by_value_key("btn_size_m")
    ADD_TO_CART_BUTTON = finder.by_value_key("btn_add_to_cart")
    
    # Flutter automatically recognizes the app bar back button!
    BACK_BUTTON = finder.page_back()

    def select_size_m(self):
        self.click_element(self.SIZE_M)

    def click_add_to_cart(self):
        self.click_element(self.ADD_TO_CART_BUTTON)

    def go_back_to_home(self):
        self.click_element(self.BACK_BUTTON)