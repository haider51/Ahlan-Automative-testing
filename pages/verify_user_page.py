from appium_flutter_finder.flutter_finder import FlutterFinder, FlutterElement

finder = FlutterFinder()

class VerifyUserPage:
    def __init__(self, driver):
        self.driver = driver

    # Locators
    CODE_INPUT = finder.by_value_key("verify_user_code")
    SUBMIT_BUTTON = finder.by_value_key("verify_user_submit")

    def is_verification_screen_visible(self):
        # This proves we successfully registered and moved to the next step!
        try:
            self.driver.execute_script('flutter:waitFor', self.CODE_INPUT, 5)
            return True
        except:
            return False