import pytest

from src.product import Product


# Фикстура для создания экземпляра продукта
@pytest.fixture
def product():
    return Product("Телефон", "Смартфон с хорошей камерой", 999.99, 10)


# Фикстура для создания словаря продукта
@pytest.fixture
def product_dict():
    return {
        "name": "Ноутбук",
        "description": "Игровой ноутбук",
        "price": 1499.99,
        "quantity": 5,
    }


def test_product_creation(product):
    assert product.name == "Телефон"
    assert product.description == "Смартфон с хорошей камерой"
    assert product.price == 999.99
    assert product.quantity == 10


def test_new_product_creation(product_dict):
    product = Product.new_product(product_dict)
    assert product.name == "Ноутбук"
    assert product.description == "Игровой ноутбук"
    assert product.price == 1499.99
    assert product.quantity == 5


def test_price_setter(product):
    product.price = 1200.00
    assert product.price == 1200.00

    product.price = -500
    assert product.price == 1200.00

    product.price = 0
    assert product.price == 1200.00


def test_str(class_product: Product) -> None:
    assert class_product.__str__() == "Iphone 15, 210000.0 руб. Остаток: 8 шт."


def test_add(class_product: Product) -> None:
    assert class_product.__add__(Product("Xiaomi", "1024GB", 31000.0, 14)) == 2114000.0
