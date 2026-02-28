from src.product import Product


# Создаем класс Category
class Category:
    # Атрибуты класса (общие для всех объектов)
    category_count = 0  # СЧЁТЧИК: сколько всего создано категорий (в __init__)
    product_count = 0  # СЧЁТЧИК: сколько всего товаров во всех категориях (в add_product)

    # Подсказки типов для атрибутов объекта (для документации)
    name: str  # У каждого объекта будет имя (строка)
    description: str  # У каждого объекта будет описание (строка)
    __products: list[Product]  # Приватный атрибут: список товаров (только внутри класса)

    def __init__(self, name, description, products=None):
        """
        Конструктор класса Category
        name - название категории
        description - описание категории
        products - список товаров (по умолчанию None)
        """
        # 1. Сохраняем публичные данные
        self.name = name  # записываем название в объект
        self.description = description  # записываем описание в объект

        # 2. Создаем приватный список (всегда пустой вначале)
        self.__products = []  # __products - два подчёркивания = приватный атрибут

        # 3. Если при создании передали список товаров
        if products is not None:  # Если products не пустой
            # Проходим по каждому товару в списке
            for product in products:  # Для каждого товара
                # Добавляем товар через специальный метод add_product
                self.add_product(product)  # Вызываем метод добавления

        # 4. Увеличиваем счетчик категорий
        Category.category_count += 1  # При создании новой категории +1

    def add_product(self, product):
        """
        Метод для добавления одного товара в категорию
        product - объект класса Product
        """
        # Проверяем, что product является экземпляром Product или его наследника
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты класса Product или его наследников")

        # Добавляем товар в приватный список
        self.__products.append(product)  # Добавляем в конец списка

        # Увеличиваем общий счетчик товаров
        Category.product_count += 1  # При добавлении одного товара +1

    @property
    # Декоратор. Он превращает обычный метод в свойство (property).
    def products(self):  # Объявление метода. Имя метода - products.
        """Возвращает строку со всеми товарами категории"""
        result = ""
        # Создаем пустую строку. В неё мы будем собирать все товары.
        # Изначально строка пустая, потому что товаров пока нет.
        for product in self.__products:  # Перебираем все товары в приватном списке __products.
            # Добавляем к результату строку с текущим товаром
            result += str(product) + "\n"
        return result  # Возвращаем готовую строку со всеми товарами.

    def __str__(self):
        """Возвращает строку с названием категории и общим количеством товаров"""
        total = 0
        for product in self.__products:
            total += product.quantity
        return f"{self.name}, количество продуктов: {total} шт."


class CategoryIterator:
    """Итератор для перебора товаров категории"""

    def __init__(self, category):
        # Сохраняем объект категории
        self.category = category
        # Индекс текущего товара (начинаем с 0)
        self._index = 0

    def __iter__(self):
        # Итератор возвращает сам себя
        return self

    def __next__(self):
        # Получаем список товаров из категории (обходим приватность)
        products = self.category._Category__products

        # Если есть ещё товары
        if self._index < len(products):
            # Берём текущий товар
            product = products[self._index]
            # Увеличиваем индекс
            self._index += 1
            return product
        else:
            # Товары закончились
            raise StopIteration
