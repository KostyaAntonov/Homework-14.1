import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def class_category() -> Category:
    return Category(
        "Смартфоны",
        "Смартфоны, как средство коммуникации "
        "и получения дополнительных функций",
        [
            Product(
                "Samsung Galaxy S23 Ultra",
                "256GB, Серый цвет, 200MP камера",
                180000.0,
                5,
                "Зеленый",
            ),
            Product("Iphone 15", "512GB, Gray space",
                    210000.0, 8, "Зеленый"),
            Product("Xiaomi Redmi Note 11", "1024GB,"
                    "Синий", 31000.0, 14, "Зеленый"),
        ],
    )


def test_init(class_category: Category) -> None:
    assert class_category.name == "Смартфоны"
    assert (
            class_category.description == "Смартфоны, как средство "
                                          "коммуникации "
                                          "и получения дополнительных функций"
    )
    assert class_category.products == (
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.Iphone 15, "
        " 210000.0 руб. Остаток: 8 шт.Xiaomi Redmi Note 11,"
        "31000.0 руб. Остаток: 14 шт."
    )
    assert class_category.category_count == 1
    assert class_category.product_count == 3


def test_add_product(class_category: Category) -> None:
    class_category.add_product(
        Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7, "Зеленый")
    )
    assert class_category.products == (
        "Samsung Galaxy S23 Ultra, 180000.0 руб. "
        "Остаток: 5 шт.Iphone 15, 210000.0 "
        "руб. Остаток: 8 шт.Xiaomi Redmi Note 11, "
        '31000.0 руб. Остаток: 14 шт.55" '
        "QLED 4K, 123000.0 руб. Остаток: 7 шт."
    )


def test_products(class_category: Category) -> None:
    assert class_category.products == (
        "Samsung Galaxy S23 Ultra, 180000.0 руб. "
        "Остаток: 5 шт.Iphone 15, 210000.0 "
        "руб. Остаток: 8 шт.Xiaomi Redmi Note 11, "
        "31000.0 руб. Остаток: 14 шт."
    )


def test_str(class_category: Category) -> None:
    assert class_category.__str__() == ("Смартфоны, количество продуктов: "
                                        "13 шт.")
