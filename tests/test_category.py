import pytest

from src.category import Category
from src.product import Product


def test_category_initialization():
    name = "Одежда"
    description = "Разная одежда"

    category = Category(name, description)

    assert category.name == "Одежда"
    assert category.description == "Разная одежда"
    assert category.products == ""  # теперь пустая строка, а не []


def test_product_count():
    Category.category_count = 0
    Category.product_count = 0

    bread = Product("Хлеб", "Свежий", 50.0, 10)
    milk = Product("Молоко", "Парное", 80.0, 5)
    water = Product("Вода", "Питьевая", 30.0, 20)

    category1 = Category("Еда", "Продукты", [bread, milk])
    category2 = Category("Напитки", "Разное питье", [water])

    assert category1.name == "Еда"
    assert category2.name == "Напитки"

    # Проверяем, что в строке есть нужные продукты
    products1 = category1.products
    assert "Хлеб" in products1
    assert "Молоко" in products1
    assert "Вода" not in products1

    products2 = category2.products
    assert "Вода" in products2
    assert "Хлеб" not in products2
    assert "Молоко" not in products2

    assert Category.product_count == 3


def test_category_count():
    Category.category_count = 0
    Category.product_count = 0

    category1 = Category("Одежда", "Разная одежда")
    category2 = Category("Обувь", "Разная обувь")
    category3 = Category("Головные уборы", "Шапки и кепки")

    assert category1.name == "Одежда"
    assert category2.name == "Обувь"
    assert category3.name == "Головные уборы"
    assert Category.category_count == 3


def test_products_private():
    """Тест, что атрибут __products действительно приватный"""
    category = Category("Одежда", "Разная одежда")

    # Пытаемся обратиться к приватному атрибуту напрямую
    with pytest.raises(AttributeError):
        # Используем getattr для обхода проверок IDE
        getattr(category, '__products')


def test_add_product():
    """Тест добавления продукта в категорию"""
    # Создаём категорию и продукт
    category = Category("Одежда", "Разная одежда")
    product = Product("Футболка", "Хлопок", 800, 10)

    # Запоминаем текущий счётчик продуктов
    old_count = Category.product_count

    # Добавляем продукт
    category.add_product(product)

    # Проверяем через геттер, что продукт появился
    products_str = category.products
    assert "Футболка" in products_str
    assert "800" in products_str
    assert "10" in products_str

    # Проверяем, что счётчик увеличился
    assert Category.product_count == old_count + 1


def test_products_getter_format():
    """Тест, что геттер products возвращает строку в нужном формате"""
    # Создаём продукты
    product1 = Product("Футболка", "Хлопок", 800, 10)
    product2 = Product("Джинсы", "Синие", 2500, 5)

    # Создаём категорию с продуктами
    category = Category("Одежда", "Разная одежда", [product1, product2])

    # Получаем строку через геттер
    result = category.products

    # Проверяем формат (каждый продукт с новой строки)
    expected = "Футболка, 800 руб. Остаток: 10 шт.\nДжинсы, 2500 руб. Остаток: 5 шт.\n"

    assert result == expected
