class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username_field = page.locator('input[name="username"]')
        self.password_field = page.locator('input[name="password"]')
        self.login_button = self.page.locator('button:has-text("Log in")')  # Updated

    def goto(self, url):
        self.page.goto(url)
        self.page.wait_for_selector('input[name="username"]')

    def login(self, username, password):
        self.username_field.fill(username)
        self.password_field.fill(password)
        self.login_button.click()
