import allure
import pytest
from pages.login_page import LogInPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage


@pytest.mark.smoke
@pytest.mark.ui

def test_add_to_cart(driver):
    login = LogInPage(driver)
    products = ProductsPage(driver)
    cart = CartPage(driver)


    with allure.step("Login with standard user"):

        login.open()
        login.login("standard_user", "secret_sauce")

    with allure.step("Add Sauce Labs Bike Light to cart"):

        products.add_product_to_cart("Sauce Labs Bike Light")

    with allure.step("Verify cart count"):

        assert products.get_cart_count() == 1
    
    with allure.step("Open cart"):

        products.go_to_cart()
    
    with allure.step(
        "Verify product exists in cart"
    ):
        assert cart.is_product_in_cart("Sauce Labs Bike Light")
    
    # assert False #- added just to make it fail for SS