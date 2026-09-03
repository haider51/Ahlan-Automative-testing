from appium_flutter_finder.flutter_finder import FlutterFinder

# Initialize the Flutter Locator tool globally for all pages to use
finder = FlutterFinder()

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click_element(self, locator):
        # Flutter's built-in wait and click commands
        self.driver.execute_script('flutter:waitFor', locator)
        self.driver.execute_script('flutter:click', locator)

    def enter_text(self, locator, text):
        self.driver.execute_script('flutter:waitFor', locator)
        self.driver.execute_script('flutter:click', locator)
        self.driver.execute_script('flutter:enterText', text)

    def is_element_visible(self, locator):
        try:
            # We wait up to 5 seconds to see if the element exists
            self.driver.execute_script('flutter:waitFor', locator, 5)
            return True
        except:
            return False
            
    def scroll_and_click_product(self, product_id):
        # Based on the Markdown file: `product_card_<id>`
        card_locator = finder.by_value_key(f"product_card_{product_id}")
        self.click_element(card_locator)