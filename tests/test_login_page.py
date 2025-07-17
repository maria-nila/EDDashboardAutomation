import pytest
from pages.login_page import LoginPage
from resource_file import TestResources
from playwright.sync_api import expect
import re

def test_valid_login(page):
    login_page = LoginPage(page)
    login_page.goto(TestResources.base_url)
    login_page.login(TestResources.valid_username, TestResources.valid_password)

    expect(page).to_have_url(re.compile(".*home"))
