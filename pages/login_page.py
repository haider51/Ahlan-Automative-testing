from appium_flutter_finder.flutter_finder import FlutterFinder, FlutterElement

finder = FlutterFinder()

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    # Keys from Markdown
    EMAIL_INPUT = finder.by_value_key("sign_in_email")
    PASSWORD_INPUT = finder.by_value_key("sign_in_password")
    LOGIN_BUTTON = finder.by_value_key("sign_in_submit")

    # The dynamic Arabic error messages (We still use by_text for these!)
    EMAIL_ERROR_MSG = finder.by_text("البريد الإلكتروني مطلوب")
    PASSWORD_ERROR_MSG = finder.by_text("كلمة المرور مطلوبة")

    def click_login(self):
        self.driver.execute_script('flutter:waitFor', self.LOGIN_BUTTON)
        element = FlutterElement(self.driver, self.LOGIN_BUTTON)
        element.click()

    def is_email_error_visible(self):
        try:
            self.driver.execute_script('flutter:waitFor', self.EMAIL_ERROR_MSG)
            return True
        except:
            return False

    def is_password_error_visible(self):
        try:
            self.driver.execute_script('flutter:waitFor', self.PASSWORD_ERROR_MSG)
            return True
        except:
            return False