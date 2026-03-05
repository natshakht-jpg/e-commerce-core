from src.base_container import BaseContainer


class Order(BaseContainer):
    """Класс заказа. Содержит один товар и его количество."""

    def __init__(self, product, quantity):
        """
        Конструктор заказа.
        product — объект класса Product (или наследника)
        quantity — количество единиц товара
        """
        self.product = product
        self.quantity = quantity

    def add_product(self, product):
        """
        Добавить товар в заказ (заменяет текущий).
        """
        self.product = product

    def total_quantity(self):
        """Возвращает количество товара в заказе."""
        return self.quantity

    def total_price(self):
        """Возвращает итоговую стоимость заказа."""
        return self.product.price * self.quantity
