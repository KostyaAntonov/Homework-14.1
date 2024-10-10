import pytest
from src.product import Product
from src.category import Category


@pytest.fixture
def sample_products():
    return [
        Product("Телефон", "Смартфон с хорошей камерой", 999.99, 10),
        Product("Ноутбук", "Игровой ноутбук", 1499.99, 5)
    ]


@pytest.fixture
def category(sample_products):
    Category.category_count = 0
    Category.product_count = 0
    return Category("Электроника", "Категория электроники", sample_products)


def test_category_initialization(category, sample_products):
    assert category.name == "Электроника"
    assert category.description == "Категория электроники"
    assert category.products == "Телефон, 999.99 руб. Остаток: 10 шт.Ноутбук, 1499.99 руб. Остаток: 5 шт."

    assert Category.category_count == 1
    assert Category.product_count == len(sample_products)


def test_add_product(category):
    new_product = Product("Планшет", "Мощный планшет", 499.99, 7)
    category.add_product(new_product)

    assert category.products == (
        "Телефон, 999.99 руб. Остаток: 10 шт."
        "Ноутбук, 1499.99 руб. Остаток: 5 шт."
        "Планшет, 499.99 руб. Остаток: 7 шт."
    )

    assert Category.product_count == 3


def test_category_count_increment():
    Category.category_count = 0
    Category.product_count = 0

    # Создадим несколько категорий
    Category("Электроника", "Категория электроники", [])
    Category("Бытовая техника", "Категория бытовой техники", [])

    assert Category.category_count == 2
