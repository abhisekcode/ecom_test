from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):

    ITEM_NAMES = (
        By.CLASS_NAME,
        "inventory_item_name"
    )

    def is_product_in_cart(self, product_name):

        items = self.driver.find_elements(
            *self.ITEM_NAMES
        )

        product_names = []

        for item in items:

            name = item.text.strip()

            product_names.append(name)

        self.logger.info(
            f"Cart products: {product_names}"
        )

        return product_name in product_names