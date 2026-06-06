from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.config_reader import load_config
from utils.logger import get_logger


class BasePage:

    def __init__(self, driver):

        self.driver = driver

        config = load_config()

        self.wait = WebDriverWait(
            driver,
            config["timeout"]
        )

        self.logger = get_logger()

    def find(self, locator):

        return self.wait.until(
            EC.visibility_of_element_located(
                locator
            )
        )

    def find_all(self, locator):

        return self.driver.find_elements(
            *locator
        )

    def click(self, locator):

        self.logger.info(
            f"Clicking on {locator}"
        )

        self.wait.until(
            EC.element_to_be_clickable(
                locator
            )
        ).click()

    def type(self, locator, text):

        self.logger.info(
            f"Typing '{text}' into {locator}"
        )

        self.find(locator).send_keys(
            text
        )