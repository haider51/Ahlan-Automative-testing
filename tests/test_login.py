from pages.home_page import HomePage
from pages.account_page import AccountPage
from pages.login_page import LoginPage

def test_empty_login_shows_errors(mobile_driver):
    home_page = HomePage(mobile_driver)
    account_page = AccountPage(mobile_driver)
    login_page = LoginPage(mobile_driver)

    # 1. Open the application on home page and navigate to account tab
    home_page.go_to_account_tab()

    # 2. Click the sign-in button
    account_page.click_sign_in_button()

    # 3. Leave the text boxes empty and click login
    login_page.click_login()

    # 4. Verify you get the two Arabic errors
    assert login_page.is_email_error_visible() == True, "Email error did not appear!"
    assert login_page.is_password_error_visible() == True, "Password error did not appear!"