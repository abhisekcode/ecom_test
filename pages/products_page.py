from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProductsPage(BasePage):

    PRODUCTS = (By.CLASS_NAME, "inventory_item")

    PRODUCT_NAME = (
        By.CLASS_NAME,
        "inventory_item_name"
    )

    CART_ICON = (
        By.CLASS_NAME,
        "shopping_cart_link"
    )

    CART_COUNT = (
        By.CLASS_NAME,
        "shopping_cart_badge"
    )

    def get_add_to_cart_button(self, product_name):

        return (
            By.XPATH,
            f"//div[text()='{product_name}']"
            f"/ancestor::div[@class='inventory_item']"
            f"//button"
        )

    def add_product_to_cart(self, product_name):

        button_locator = (
            self.get_add_to_cart_button(
                product_name
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            self.find(button_locator)
        )

        self.logger.info(
            f"Added product: {product_name}"
        )

    def get_cart_count(self):

        count = self.find(
            self.CART_COUNT
        ).text

        return int(count)

    def go_to_cart(self):

        self.click(
            self.CART_ICON
        )