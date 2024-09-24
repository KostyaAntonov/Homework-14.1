from src.product import Product


class Category:
    name: str
    description: str
    category_count = 0
    product_count = 0

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.products = []
        Category.category_count += 1

    def add_product(self, product):
        self.products.append(product)
        Category.product_count += 1


smartphones = Category(
    "Смартфоны",
    "Смартфоны, как средство не только коммуникации, "
    "но и получение дополнительных функций для удобства жизни",
)

smartphones.add_product(
    Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
)
smartphones.add_product(Product("Iphone 15", "512GB, Gray space", 210000.0, 8))
smartphones.add_product(Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14))

televisions = Category(
    "Телевизоры",
    "Современный телевизор, который позволяет "
    "наслаждаться просмотром, станет вашим другом и помощником",
)

televisions.add_product(Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7))
