# tests/test_cart.py

from pages.home_page import HomePage
from pages.product_details_page import ProductDetailsPage
from pages.cart_page import CartPage

def test_add_clothing_to_cart(mobile_driver):
    home_page = HomePage(mobile_driver)
    product_page = ProductDetailsPage(mobile_driver)
    cart_page = CartPage(mobile_driver)

    # 1. Select clothing item on the home page
    home_page.select_pajama_product()

    # 2. Select Size M and tap "Add to Cart"
    product_page.select_size_m()
    product_page.click_add_to_cart()

    # 3. Return to home and open Cart
    product_page.go_back_to_home()
    home_page.open_cart_from_bottom_nav()

    # 4. Verify product exists in the shopping cart
    assert cart_page.is_product_in_cart() == True, "The pajama was not added to the cart!"