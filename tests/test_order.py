from src.order import Order
from src.product import Product


def test_order_initialization():
    """Тест создания заказа."""
    product = Product("Футболка", "Хлопок", 800, 10)
    order = Order(product, 3)

    assert order.product == product
    assert order.quantity == 3


def test_order_total_quantity():
    """Тест получения количества товара в заказе."""
    product = Product("Футболка", "Хлопок", 800, 10)
    order = Order(product, 3)

    assert order.total_quantity() == 3


def test_order_total_price():
    """Тест расчёта итоговой стоимости заказа."""
    product = Product("Футболка", "Хлопок", 800, 10)
    order = Order(product, 3)

    assert order.total_price() == 800 * 3


def test_order_add_product():
    """Тест замены товара в заказе."""
    p1 = Product("Футболка", "Хлопок", 800, 10)
    p2 = Product("Джинсы", "Синие", 2500, 5)
    order = Order(p1, 3)

    order.add_product(p2)  # заменяем товар
    assert order.product == p2
    assert order.quantity == 3  # количество не меняется
