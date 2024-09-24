import pytest

from src.product import Product


@pytest.fixture
def product():
    return Product("Apple", "A delicious fruit", 1.50, 10)


def test_product_creation(product):
    assert product.name == "Apple"
    assert product.description == "A delicious fruit"
    assert product.price == 1.50
    assert product.quantity == 10


def test_product_attributes(product):
    assert hasattr(product, "name")
    assert hasattr(product, "description")
    assert hasattr(product, "price")
    assert hasattr(product, "quantity")
