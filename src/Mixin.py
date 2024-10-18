class Mixin:
    """Класс-миксин, который будет печатать в консоль информацию о том,
    от какого класса и скакими параметрами был создан объект"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self) -> None:
        print(repr(self))

    def __repr__(self) -> str:
        return (f"{self.__class__.__name__}({self.name}, "
                f"{self.description}, {self.price}, {self.quantity})")
