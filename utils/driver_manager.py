from selenium import webdriver
from utils.config_reader import load_config
from selenium.webdriver.chrome.options import Options


class DriverManager:

    @staticmethod
    def get_driver(browser, headless):

        # config = load_config()
        # browser = config["browser"]

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
            driver = webdriver.Edge()

        else:
            raise Exception("Browser not supported")
        
        driver.maximize_window()
        return driver