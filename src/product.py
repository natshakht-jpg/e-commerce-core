from src.base_product import BaseProduct
from src.mixin import ProductPrintMixin


class ZeroQuantityError(Exception):
    """Исключение при попытке создать товар с нулевым количеством"""
    pass


# Основной класс товара (с миксин и абстрактной базой)
class Product(ProductPrintMixin, BaseProduct):
    # Определяем поля (свойства) класса
    name: str
    description: str
    quantity: int

    # Создаем конструктор класса, который принимает данные для создания объекта
    def __init__(self, name, description, price, quantity):
        # Проверка на нулевое количество
        if quantity <= 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")

        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__()  # вызов родителя (миксина)

    @classmethod  # Декоратор. Превращает обычный метод в класс-метод.
    def new_product(cls, product_data, products_list=None):
        # Добавился параметр products_list - список существующих товаров
        """
        Создаёт новый продукт или обновляет существующий
        product_data - словарь с данными
        products_list - список существующих товаров (может не передаваться)
        """
        name = product_data["name"]  # Достаем из словаря значение по ключу "name" и сохраняем в переменную name

        if products_list is not None:
            for existing_product in products_list:  # Проверяем, есть ли товар с таким же именем в списке
                if existing_product.name == name:
                    # Если есть дубликат - обновляем количество и цену
                    existing_product.quantity += product_data["quantity"]
                    if product_data["price"] > existing_product.price:
                        existing_product.price = product_data["price"]
                    return existing_product  # возвращаем старый товар

        # Если дубликата нет - создаём новый товар
        description = product_data["description"]
        price = product_data["price"]
        quantity = product_data["quantity"]
        return cls(name, description, price, quantity)

    @property
    def price(self):  # Геттер для цены
        return self.__price

    @price.setter  # Декоратор сеттера для свойства price.
    def price(self, new_price):
        # Определение метода-сеттера.
        # self - ссылка на текущий объект
        # new_price - новое значение цены, которое пытаются установить
        if new_price <= 0:  # Проверяем условие: если новая цена меньше или равна нулю
            # (то есть 0 или отрицательное число)
            print("Цена не должна быть нулевая или отрицательная")
            # Выводим сообщение об ошибке в консоль
            # Цена не меняется, просто предупреждаем пользователя
            return

        if new_price < self.__price:
            # Запрашиваем подтверждение у пользователя
            answer = input(f"Понизить цену с {self.__price} до {new_price}? (y/n): ")

            if answer.lower() == "y":
                self.__price = new_price
                print("Цена обновлена")
            else:
                print("Понижение цены отменено")

        else:  # Если цена не понижается (больше или равна)
            self.__price = new_price  # Присваиваем новое значение приватному атрибуту __price.
            print("Цена обновлена")  # Теперь цена обновлена

    def __str__(self):
        """Возвращает строковое представление продукта.
        Формат: Название, цена руб. Остаток: количество шт."""
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Возвращает сумму стоимости всех товаров на складе для двух продуктов"""
        if type(self) is not type(other):  # проверка на одинаковый класс
            raise TypeError("Нельзя складывать товары разных классов")

        return self.__price * self.quantity + other.__price * other.quantity


class Smartphone(Product):
    """Создаем класс «Смартфон» (Smartphone) наследник класса Product"""
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        # Вызываем родительский конструктор для общих атрибутов
        super().__init__(name, description, price, quantity)

        # Добавляем свои новые атрибуты
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """Создаем класс «Трава газонная» (LawnGrass) наследник класса Product"""
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        # Вызываем родительский конструктор для общих атрибутов
        super().__init__(name, description, price, quantity)

        # Добавляем свои новые атрибуты
        self.country = country
        self.germination_period = germination_period
        self.color = color
