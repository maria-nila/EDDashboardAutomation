import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.dashboard_page import DashboardPage
from resource_file import TestResources
from playwright.sync_api import expect
import re

def test_view_dashboard_happy_path(page):
    login_page = LoginPage(page)
    login_page.goto(TestResources.base_url)
    login_page.login(TestResources.valid_username, TestResources.valid_password)

    expect(page).to_have_url(re.compile(".*home"))

    home_page = HomePage(page)
    home_page.click_view_dashboard()

    expect(page).to_have_url(re.compile(".*dashboard"))

    dashboard_page = DashboardPage(page)
    assert dashboard_page.is_loaded()