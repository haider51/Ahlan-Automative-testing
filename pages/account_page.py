from appium_flutter_finder.flutter_finder import FlutterFinder, FlutterElement

finder = FlutterFinder()

class AccountPage:
    def __init__(self, driver):
        self.driver = driver

    GOTO_SIGN_IN_BUTTON = finder.by_value_key("dashboard_sign_in_link")
    GOTO_SIGN_UP_BUTTON = finder.by_value_key("dashboard_sign_up") # <--- ADDED

    def click_sign_in_button(self):
        self.driver.execute_script('flutter:waitFor', self.GOTO_SIGN_IN_BUTTON)
        element = FlutterElement(self.driver, self.GOTO_SIGN_IN_BUTTON)
        element.click()

    def click_sign_up_button(self):
        self.driver.execute_script('flutter:waitFor', self.GOTO_SIGN_UP_BUTTON)
        element = FlutterElement(self.driver, self.GOTO_SIGN_UP_BUTTON)
        element.click()