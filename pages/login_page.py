from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.config_reader import load_config


class LogInPage(BasePage):

    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID,"login-button")

    def open(self):

        config = load_config()

        self.driver.get(
            config["base_url"]
        )

    def login(self, username, password):

        self.type(self.USERNAME, username)

        self.type(self.PASSWORD, password)

        self.click(self.LOGIN_BTN)

    def is_logged_in(self):

        return "inventory" in self.driver.current_url