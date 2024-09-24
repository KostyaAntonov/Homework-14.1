import pytest

from src.category import Category
from src.product import Product


@pytest.fixture(autouse=True)
def reset_category_counts():
    Category.category_count = 0
    Category.product_count = 0


@pytest.fixture
def product():
    return Product(
        "Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )


@pytest.fixture
def category():
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, "
        "но и получение дополнительных функций для удобства жизни",
    )


def test_category_creation(category):
    assert category.name == "Смартфоны"
    assert (
        category.description
        == "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни"
    )
    assert category.products == []
    assert Category.category_count == 1


def test_add_product(category, product):
    category.add_product(product)
    assert len(category.products) == 1
    assert category.products[0] == product
    assert Category.product_count == 1


def test_category_count(category):
    assert Category.category_count == 1
