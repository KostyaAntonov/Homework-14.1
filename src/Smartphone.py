from typing import Any

from src.product import Product


class Smartphone(Product):
    """Класс, который представляет смартфоны"""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ):
        super().__init__(name, description, price, quantity, color)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory

    def __add__(self, other: "Product") -> Any:
        if type(other) is Smartphone:
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError
