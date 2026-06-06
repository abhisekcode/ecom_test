from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProductsPage(BasePage):

    PRODUCTS = (By.CLASS_NAME, "inventory_item")
    PRODUCT_NAME = (By.CLASS_NAME, "inventory_item_name")

    CART_ICON = (
        By.CLASS_NAME,
        "shopping_cart_link"
    )

    CART_COUNT = (
        By.CLASS_NAME,
        "shopping_cart_badge"
    )

    # ADD_TO_CART_BUTTON = (
    #     By.CLASS_NAME,
    #     "btn_inventory"
    # )

    def get_add_to_cart_button(self, product_name):

        return (
            By.XPATH,

            f"//div[text()='{product_name}']"
            f"/ancestor::div[@class='inventory_item']"
            f"//button"
        )

    def add_product_to_cart(self, product_name):

        # products = self.find_all(self.PRODUCTS)

        # for product in products:

        #     name = product.find_element(
        #         *self.PRODUCT_NAME
        #     ).text

        #     self.logger.info(
        #         f"Found product: {name}"
        #     )

        #     if name.strip() == product_name.strip():

        #         button = product.find_element(
        #             *self.ADD_TO_CART_BUTTON
        #         )

        #         button.click()

        #         self.logger.info(
        #             f"Clicked Add to Cart for {name}"
        #         )

        #         return

        # raise Exception(
        #     f"Product not found: {product_name}"
        # )
        self.click(
            self.get_add_to_cart_button(product_name)
        )

        self.driver.save_screenshot(
            "after_click.png"
        )
        
        button = self.find(
            self.get_add_to_cart_button(product_name)
        )
        
        self.logger.info(
            f"Button text after click: {button.text}"
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

        self.click(self.CART_ICON)