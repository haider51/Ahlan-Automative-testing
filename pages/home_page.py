from appium_flutter_finder.flutter_finder import FlutterFinder, FlutterElement

finder = FlutterFinder()

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    # Key from Markdown: tab_account
    ACCOUNT_TAB = finder.by_value_key("tab_account")

    def go_to_account_tab(self):
        self.driver.execute_script('flutter:waitFor', self.ACCOUNT_TAB)
        element = FlutterElement(self.driver, self.ACCOUNT_TAB)
        element.click()