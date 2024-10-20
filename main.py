from src.category import Category
from src.product import Product

if __name__ == "__main__":

    try:
        product_invalid = Product("Бракованный товар", "Неверное количество", 1000.0, 0, "grey")
    except ValueError as e:
        print(e)
    else:
        print("Не возникла ошибка ValueError при попытке добавить продукт с нулевым количеством")

    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, "grey")
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8, "grey")
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, "grey")

    category1 = Category("Смартфоны", "Категория смартфонов", [product1, product2, product3])

    print(category1.price_value())

    category_empty = Category("Пустая категория", "Категория без продуктов", [])
    print(category_empty.price_value())
