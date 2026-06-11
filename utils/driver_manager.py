from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions


class DriverManager:

    @staticmethod
    def get_driver(browser, headless):

        if browser == "chrome":

            options = Options()

            if headless:
                options.add_argument("--headless=new")
                options.add_argument("--no-sandbox")
                options.add_argument("--disable-dev-shm-usage")
                options.add_argument("--window-size=1920,1080")

            driver = webdriver.Chrome(
                options=options
            )

        elif browser == "edge":

            options = EdgeOptions()

            if headless:
                options.add_argument("--headless=new")
                options.add_argument("--no-sandbox")
                options.add_argument("--disable-dev-shm-usage")
                options.add_argument("--window-size=1920,1080")

            driver = webdriver.Edge(
                options=options
            )

        elif browser == "firefox":

            options = FirefoxOptions()

            if headless:
                options.add_argument("-headless")

            driver = webdriver.Firefox(
                options=options
            )

        else:
            raise Exception(
                "Browser not supported"
            )

        if not headless:
            driver.maximize_window()

        return driver