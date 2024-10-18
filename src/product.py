from typing import Any

from src.BaseProduct import BaseProduct
from src.Mixin import Mixin


class Product(Mixin, BaseProduct):
    """Класс, который представляет продукты"""

    def __init__(
            self, name: str, description: str,
            price: float, quantity: int, color: str
    ):
        """Метод, который инициализирует экземпляры класса"""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        self.color = color
        super().__init__()

    @classmethod
    def new_product(cls, product_dict: dict) -> "Product":
        name, description, price, quantity, color = product_dict.values()
        return cls(name, description, price, quantity, color)

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, price: float) -> None:
        if price == 0 or price < 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = price

    def __str__(self) -> str:
        """Выводит продукт, цена и остаток"""
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> Any:
        """Возвращает сумму произведений цены
        на количество для двух объектов"""
        if type(other) is Product:
            return self.__price * self.quantity + other.price * other.quantity
        raise TypeError
