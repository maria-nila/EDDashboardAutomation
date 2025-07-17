class HomePage:
    def __init__(self, page):
        self.page = page
        self.view_dashboard_button = page.locator('a.btn.btn-success[href="/dashboard/view_dashboard/"]')

    def click_view_dashboard(self):
        self.view_dashboard_button.click()
