import re
from playwright.sync_api import expect, Page
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.dashboard_page import DashboardPage
from resource_file import TestResources

def test_dashboard_filters(page: Page):
    # Login
    login_page = LoginPage(page)
    login_page.goto(TestResources.base_url)
    login_page.login(TestResources.valid_username, TestResources.valid_password)

    expect(page).to_have_url(re.compile(".*home"))

    # Navigate to dashboard
    home_page = HomePage(page)
    home_page.click_view_dashboard()

    expect(page).to_have_url(re.compile(".*dashboard"))

    # Interact with filters
    dashboard_page = DashboardPage(page)
    dashboard_page.open_filters()
    dashboard_page.select_operation_type("Microfinance")
    dashboard_page.select_program_name("Microfinance")
    dashboard_page.select_project_name("Microfinance")
    dashboard_page.select_project_status("Active")
    dashboard_page.apply_filters()

    # Optional: Download and close
    dashboard_page.download_brac_programme_coverage()
    dashboard_page.close_filters()
