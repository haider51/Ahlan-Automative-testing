from pages.base_page import BasePage, finder

class CartPage(BasePage):
    
    def is_product_in_cart(self, product_id="123"):
        # Checking if the product card ID appears inside the cart screen
        CART_ITEM = finder.by_value_key(f"cart_item_{product_id}")
        return self.is_element_visible(CART_ITEM)