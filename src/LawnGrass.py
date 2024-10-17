from typing import Any

from src.product import Product


class LawnGrass(Product):
    """Класс, который предтавляет траву газонную"""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ):
        super().__init__(name, description, price, quantity, color)
        self.country = country
        self.germination_period = germination_period

    def __add__(self, other: "Product") -> Any:
        if type(other) is LawnGrass:
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError
