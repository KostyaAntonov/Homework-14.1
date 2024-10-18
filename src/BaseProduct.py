from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный класс, который является родительским для класса продуктов"""

    @abstractmethod
    def __init__(self) -> None:
        pass
