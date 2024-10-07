from src.category import Category
from src.product import Product

if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(product1.name, product1.description, product1.price, product1.quantity, sep='\n')
    print()
    print(product2.name, product2.description, product2.price, product2.quantity, sep='\n')
    print()
    print(product3.name, product3.description, product3.price, product3.quantity, sep='\n')
    print()

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    print(category1.name, category1.description, len(category1.products), category1.category_count,
          category1.product_count, sep='\n')
    print()

    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category2 = Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [product4],
    )

    print(category2.name, category2.description, len(category2.products), category2.products, sep='\n')
    print()

    print(Category.category_count)
    print(Category.product_count)
