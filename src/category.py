from src.product import Product


class Category:
    """Класс, который представляет категории"""

    category_count = None
    product_count = None

    def __init__(self, name: str, description: str, products: list):
        """Метод, который инициализирует экземпляры класса"""

        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product: Product) -> None:
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        str_products = ""
        for product in self.__products:
            str_products += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."
        return str_products
