from appium_flutter_finder.flutter_finder import FlutterFinder, FlutterElement

finder = FlutterFinder()

class RegisterPage:
    def __init__(self, driver):
        self.driver = driver

    FIRST_NAME = finder.by_value_key("register_first_name")
    LAST_NAME = finder.by_value_key("register_last_name")
    EMAIL = finder.by_value_key("register_email")
    PASSWORD = finder.by_value_key("register_password")
    CONFIRM_PASSWORD = finder.by_value_key("register_confirm_password")
    
    # THE CHECKBOX:
    TERMS_CHECKBOX = finder.by_value_key("register_newsletter")
    
    SUBMIT_BUTTON = finder.by_value_key("register_submit")
    SIGN_IN_LINK = finder.by_value_key("register_sign_in_link")

    def enter_first_name(self, name):
        self.driver.execute_script('flutter:waitFor', self.FIRST_NAME)
        element = FlutterElement(self.driver, self.FIRST_NAME)
        element.click()
        element.clear()
        element.send_keys(name)

    def enter_last_name(self, name):
        self.driver.execute_script('flutter:waitFor', self.LAST_NAME)
        element = FlutterElement(self.driver, self.LAST_NAME)
        element.click()
        element.clear()
        element.send_keys(name)

    def enter_email(self, email):
        self.driver.execute_script('flutter:waitFor', self.EMAIL)
        element = FlutterElement(self.driver, self.EMAIL)
        element.click()
        element.clear()
        element.send_keys(email)

    def enter_password(self, password):
        self.driver.execute_script('flutter:waitFor', self.PASSWORD)
        element = FlutterElement(self.driver, self.PASSWORD)
        element.click()
        element.clear()
        element.send_keys(password)

    def enter_confirm_password(self, password):
        self.driver.execute_script('flutter:waitFor', self.CONFIRM_PASSWORD)
        element = FlutterElement(self.driver, self.CONFIRM_PASSWORD)
        element.click()
        element.clear()
        element.send_keys(password)

    # ACTION TO CLICK THE CHECKBOX:
    def click_terms_checkbox(self):
        self.driver.execute_script('flutter:waitFor', self.TERMS_CHECKBOX)
        element = FlutterElement(self.driver, self.TERMS_CHECKBOX)
        element.click()

    def click_submit(self):
        self.driver.execute_script('flutter:waitFor', self.SUBMIT_BUTTON)
        element = FlutterElement(self.driver, self.SUBMIT_BUTTON)
        element.click()

    def click_sign_in_link(self):
        self.driver.execute_script('flutter:waitFor', self.SIGN_IN_LINK)
        element = FlutterElement(self.driver, self.SIGN_IN_LINK)
        element.click()

    def is_still_on_register_page(self):
        try:
            self.driver.execute_script('flutter:waitFor', self.SUBMIT_BUTTON, 2)
            return True
        except:
            return False