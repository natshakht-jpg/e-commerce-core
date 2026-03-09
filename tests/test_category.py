import pytest

from src.category import Category, CategoryIterator
from src.product import Product, Smartphone


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


def test_category_str():
    """Тест строкового представления категории"""
    p1 = Product("Футболка", "Хлопок", 800, 10)
    p2 = Product("Джинсы", "Синие", 2500, 5)
    category = Category("Одежда", "Разная одежда", [p1, p2])

    expected = "Одежда, количество продуктов: 15 шт."
    assert str(category) == expected


def test_category_iterator():
    """Тест итератора для перебора товаров категории"""
    p1 = Product("Футболка", "Хлопок", 800, 10)
    p2 = Product("Джинсы", "Синие", 2500, 5)
    category = Category("Одежда", "Разная одежда", [p1, p2])

    # Собираем все товары из итератора в список
    products_from_iterator = []
    for product in CategoryIterator(category):
        products_from_iterator.append(product)

    # Проверяем, что вернулись все товары
    assert len(products_from_iterator) == 2
    assert products_from_iterator[0].name == "Футболка"
    assert products_from_iterator[1].name == "Джинсы"


def test_add_product_with_inheritance():
    """Тест добавления объектов-наследников в категорию"""
    category = Category("Тест", "Описание")
    smartphone = Smartphone("Тест", "Описание", 1000, 5, "95.5", "Модель", 256, "Черный")

    category.add_product(smartphone)

    # Проверяем, что продукт добавился
    assert str(smartphone) in category.products


def test_add_non_product():
    """Тест добавления объекта не-продукта (должна быть ошибка)"""
    category = Category("Тест", "Описание")

    with pytest.raises(TypeError):
        category.add_product("Это строка, а не продукт")


def test_category_total_quantity():
    """Тест подсчёта общего количества товаров в категории."""
    p1 = Product("Футболка", "Хлопок", 800, 10)
    p2 = Product("Джинсы", "Синие", 2500, 5)
    category = Category("Одежда", "Разная одежда", [p1, p2])

    assert category.total_quantity() == 15


def test_category_total_price():
    """Тест подсчёта общей стоимости товаров в категории."""
    p1 = Product("Футболка", "Хлопок", 800, 10)
    p2 = Product("Джинсы", "Синие", 2500, 5)
    category = Category("Одежда", "Разная одежда", [p1, p2])

    expected = 800 * 10 + 2500 * 5  # 8000 + 12500 = 20500
    assert category.total_price() == expected


def test_middle_price_with_products():
    """Метод возвращает правильную среднюю цену, когда есть товары"""
    p1 = Product("Футболка", "Хлопок", 800, 10)
    p2 = Product("Джинсы", "Синие", 2500, 5)
    category = Category("Одежда", "Разная одежда", [p1, p2])

    assert category.middle_price() == 1650


def test_middle_price_empty_category():
    """Метод возвращает 0, если категория пуста"""
    # Создаём категорию без товаров
    category = Category("Пустая категория", "Описание")

    # Проверяем, что метод возвращает 0
    assert category.middle_price() == 0
