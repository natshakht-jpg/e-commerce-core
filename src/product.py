# Создаем класс Product
class Product:
    # Определяем поля (свойства) класса
    name: str
    description: str
    price: float
    quantity: int

    # Создаем конструктор класса, который принимает данные для создания объекта
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
