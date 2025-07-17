from playwright.sync_api import expect

class DashboardPage:
    def __init__(self, page):
        self.page = page

        # Button locators
        self.filters_button = page.locator("xpath=//*[@id='kt_explore_toggle_label']")
        self.apply_button = page.locator("xpath=//*[@id='filter_button']")
        self.close_button = page.locator("xpath=/html/body/div[1]/div[2]/div/div[2]/div[2]/div[1]/div/div[1]/div/button")  # ⛔️ Keep it simple if possible
        self.download_button = page.locator("xpath=//*[@id='btn_download_excel']")

        # Select2 dropdowns
        self.operation_type_select2 = page.locator("xpath=//label[contains(text(),'Operation Type')]/following::span[contains(@class,'select2-selection')][1]")
        self.program_name_select2 = page.locator("xpath=//label[contains(text(),'Program Name')]/following::span[contains(@class,'select2-selection')][1]")
        self.project_name_select2 = page.locator("xpath=//label[contains(text(),'Project Name')]/following::span[contains(@class,'select2-selection')][1]")
        self.project_status_select2 = page.locator("xpath=//label[contains(text(),'Project Status')]/following::span[contains(@class,'select2-selection')][1]")

    def open_filters(self):
        print("Clicking filter button...")
        self.filters_button.click()
        expect(self.operation_type_select2).to_be_visible(timeout=10000)
        print("Filter panel is visible.")

    def select_select2_option(self, select2_container, option_text):
        select2_container.click()
        dropdown_option = self.page.locator(f".select2-results__option:has-text('{option_text}')")
        dropdown_option.click()
        print(f"Selected: {option_text}")

    def select_operation_type(self, value):
        self.select_select2_option(self.operation_type_select2, value)

    def select_program_name(self, value):
        self.select_select2_option(self.program_name_select2, value)

    def select_project_name(self, value):
        self.select_select2_option(self.project_name_select2, value)

    def select_project_status(self, value):
        self.select_select2_option(self.project_status_select2, value)

    def apply_filters(self):
        print("Applying filters...")
        self.apply_button.click()

    def close_filters(self):
        print("Closing filter panel...")
        self.close_button.click()

    def download_brac_programme_coverage(self):
        print("Downloading Excel file...")
        self.download_button.click()
