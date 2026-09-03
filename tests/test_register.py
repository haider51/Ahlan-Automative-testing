import pytest
import time
from pages.home_page import HomePage
from pages.account_page import AccountPage
from pages.register_page import RegisterPage
from pages.verify_user_page import VerifyUserPage

class TestRegistration:

    # --- TC_REGISTER_001: Happy Path ---
    def test_happy_path_registration(self, mobile_driver):
        home_page = HomePage(mobile_driver)
        account_page = AccountPage(mobile_driver)
        register_page = RegisterPage(mobile_driver)
        verify_page = VerifyUserPage(mobile_driver)

        home_page.go_to_account_tab()
        account_page.click_sign_up_button()

        unique_email = f"qa_test_{int(time.time())}@ahlanmarket.net"

        register_page.enter_first_name("QA")
        register_page.enter_last_name("Tester")
        register_page.enter_email(unique_email)
        register_page.enter_password("Pass12345!")
        register_page.enter_confirm_password("Pass12345!")
        
        # Click the Checkbox!
        register_page.click_terms_checkbox()
        
        register_page.click_submit()

        assert verify_page.is_verification_screen_visible() == True, "Did not reach OTP screen!"

    # --- TC_REGISTER_002, 003, 004: Validation Errors (Parameterized!) ---
    @pytest.mark.parametrize("fname, lname, email, pwd, confirm_pwd, scenario", [
        ("", "", "", "", "", "Empty Fields"),
        ("QA", "Tester", "valid@ahlan.net", "Pass123@@", "WrongPass", "Password Mismatch"),
        ("QA", "Tester", "invalid-email-format", "Pass123@@", "Pass123@@", "Invalid Email"),
    ])
    def test_registration_validation_errors(self, mobile_driver, fname, lname, email, pwd, confirm_pwd, scenario):
        home_page = HomePage(mobile_driver)
        account_page = AccountPage(mobile_driver)
        register_page = RegisterPage(mobile_driver)

        home_page.go_to_account_tab()
        account_page.click_sign_up_button()

        if fname: register_page.enter_first_name(fname)
        if lname: register_page.enter_last_name(lname)
        if email: register_page.enter_email(email)
        if pwd: register_page.enter_password(pwd)
        if confirm_pwd: register_page.enter_confirm_password(confirm_pwd)

        # Click the Checkbox!
        register_page.click_terms_checkbox()

        register_page.click_submit()

        assert register_page.is_still_on_register_page() == True, f"Failed on scenario: {scenario}"