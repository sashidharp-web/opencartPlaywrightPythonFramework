from playwright.sync_api import expect

import config
from pages import home_page, login_page, my_account_page, logout_page
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.my_account_page import MyAccountPage
from pages.logout_page import LogoutPage
import pytest

from config import Config

@pytest.mark.regression
def test_user_logout(page):
    home_page=HomePage(page)
    login_page=LoginPage(page)
    my_account_page=MyAccountPage(page)
    logout_page=LogoutPage(page)

    #Click Login and enter the details
    home_page.click_my_account()
    home_page.click_login()
    login_page.login(Config.email,Config.password)
    #login_page.click_login()

    page.wait_for_timeout(5000)

    #verify whether User's home page is displayed
    expect(my_account_page.get_my_account_page_heading()).to_be_visible(timeout=3000)

    #click Logout and Continue to return to home page
    my_account_page.click_logout()
    expect(logout_page.get_continue_button()).to_be_visible(timeout=3000)
    logout_page.click_continue()

    #verify home page
    expect(page).to_have_title("Your Store")

