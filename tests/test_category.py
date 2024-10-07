import pytest

from tests.test_product import product1, product2, product3


class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.products = products
        Category.category_count += 1
        Category.product_count += len(products)


@pytest.fixture
def category1(product1, product2, product3):
    Category.category_count = 0
    Category.product_count = 0
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )


def test_category_creation(category1, product1, product2, product3):
    assert category1.name == "Смартфоны"
    assert category1.description == ("Смартфоны, как средство не только коммуникации, но и получения дополнительных "
                                     "функций для удобства жизни")
    assert category1.products == [product1, product2, product3]


def test_category_count(category1):
    assert Category.category_count == 1


def test_product_count(category1):
    assert Category.product_count == 3
