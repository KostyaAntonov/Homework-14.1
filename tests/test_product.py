import pytest

from src.product import Product
from src.Smartphone import Smartphone


@pytest.fixture
def class_product() -> Product:
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8, "Зеленый")


def test_init(class_product: Product) -> None:
    assert class_product.name == "Iphone 15"
    assert class_product.description == "512GB, Gray space"
    assert class_product.price == 210000.0
    assert class_product.quantity == 8
    assert class_product.color == "Зеленый"


def test_new_product(class_product: Product) -> None:
    class_product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
            "color": "Зеленый"
        }
    )
    assert class_product


@pytest.mark.parametrize("price1, price2", ([100, 100], [-100, 210000.0]))
def test_price(class_product: Product, price1: float, price2: float) -> None:
    class_product.price = price1
    assert class_product.price == price2


def test_str(class_product: Product) -> None:
    assert class_product.__str__() == "Iphone 15, 210000.0 руб. Остаток: 8 шт."


def test_add(class_product: Product) -> None:
    assert class_product.__add__(Product("Xiaomi", "1024GB", 31000.0, 14, "Зеленый")) == 2114000.0


def test_add_with_mistake(class_product: Product) -> None:
    smartphone2 = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
    with pytest.raises(TypeError):
        class_product + smartphone2
