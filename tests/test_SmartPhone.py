import pytest

from src.LawnGrass import LawnGrass
from src.Smartphone import Smartphone


@pytest.fixture
def class_smartphone() -> Smartphone:
    return Smartphone(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
        95.5,
        "S23 Ultra",
        256,
        "Серый",
    )


def test_init(class_smartphone: Smartphone) -> None:
    assert class_smartphone.name == "Samsung Galaxy S23 Ultra"
    assert class_smartphone.description == "256GB, Серый цвет, 200MP камера"
    assert class_smartphone.price == 180000.0
    assert class_smartphone.quantity == 5
    assert class_smartphone.efficiency == 95.5
    assert class_smartphone.model == "S23 Ultra"
    assert class_smartphone.memory == 256
    assert class_smartphone.color == "Серый"


def test_add(class_smartphone: Smartphone) -> None:
    assert (
        class_smartphone.__add__(
            Smartphone(
                "Samsung Galaxy S23 Ultra",
                "256GB, Серый цвет, 200MP камера",
                180000.0,
                5,
                95.5,
                "S23 Ultra",
                256,
                "Серый",
            )
        )
        == 1800000.0
    )


def test_add_with_mistake(class_smartphone: Smartphone) -> None:
    grass1 = LawnGrass(
        "Газонная трава",
        "Элитная трава для газона",
        500.0,
        20,
        "Россия",
        "7 дней",
        "Зеленый",
    )
    with pytest.raises(TypeError):
        class_smartphone + grass1
