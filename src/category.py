# Создаем класс Category
class Category:
    # Атрибуты класса (общие для всех)
    category_count = 0
    product_count = 0

    # Атрибуты объекта (поля)
    name: str
    description: str
    products: list

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.products = products if products is not None else []

        # Увеличиваем счетчики
        Category.category_count += 1
        Category.product_count += len(self.products)
