import json

from src.category import Category
from src.product import Product


def load_from_json(file_path: str):
    """
    Загружает данные из JSON-файла и создает объекты Category и Product.

    Аргументы:
        file_path (str): Путь к JSON-файлу

    Возвращает:
        list: Список объектов Category с вложенными объектами Product
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    categories = []

    # Проходим по каждой категории в файле
    for category_data in data:
        # Создаем продукты для этой категории
        product_objects = []
        for product_data in category_data['products']:
            product = Product(
                product_data['name'],
                product_data['description'],
                product_data['price'],
                product_data['quantity']
            )
            product_objects.append(product)

        # Создаем категорию
        category = Category(
            category_data['name'],
            category_data['description'],
            product_objects
        )
        categories.append(category)

    return categories
