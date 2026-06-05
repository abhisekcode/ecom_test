from data.product_mapping import UI_TO_API_MAP
from utils.db_utils import insert_product, get_products, clear_cart
from pages.login_page import LogInPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
import requests
import json
import pytest

@pytest.mark.parametrize("product_name", [
    "Sauce Labs Backpack",
    "Sauce Labs Bike Light"
])

@pytest.mark.regression
def test_ui_db_integration(driver, product_name):

    with open("data/test_data.json") as f:
        data = json.load(f)

    #product_name = data["products"][0]

    clear_cart()

    login = LogInPage(driver)
    products = ProductsPage(driver)
    cart = CartPage(driver)

    # Step 1: UI actions
    login.open()
    login.login("standard_user", "secret_sauce")

    products.add_product_to_cart(product_name)
    
    assert products.get_cart_count() == 1
    products.go_to_cart()

    # Step 2: UI validation
    assert cart.is_product_in_cart(product_name)

    # Step 3: API validation (✅ MUST be inside function)
    api_product = UI_TO_API_MAP[product_name]

    response = requests.get("https://dummyjson.com/products")
    data = response.json()

    api_products = [p["title"] for p in data["products"]]

    assert api_product in api_products

    # Step 4: Store in DB
    insert_product(product_name)

    # Step 5: DB validation
    db_products = get_products()

    assert product_name in db_products
    