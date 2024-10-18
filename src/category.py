from src.product import Product


class Category:
    """Класс, который представляет категории"""

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list):
        """Метод, который инициализирует экземпляры класса"""

        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product: Product) -> None:
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError

    @property
    def products(self) -> str:
        str_products = ""
        for product in self.__products:
            str_products += (
                f"{product.name}, {product.price} руб. "
                f"Остаток: {product.quantity} шт."
            )
        return str_products

    def __str__(self) -> str:
        """Выводит общее количество товаров"""
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."
