import requests
import pytest


@pytest.mark.api
@pytest.mark.smoke

def test_get_products():

    try:
        response = requests.get("https://dummyjson.com/products", timeout=5)
    except requests.exceptions.RequestException:
        pytest.skip("API not reachable")

    assert response.status_code == 200

    data = response.json()

    assert "products" in data

    assert len(data["products"])>0

    assert "title" in data["products"][0]