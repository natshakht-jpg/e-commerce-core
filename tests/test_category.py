from src.category import Category
from src.product import Product


def test_category_initialization():
    name = "Одежда"
    description = "Разная одежда"

    category = Category(name, description)

    assert category.name == "Одежда"
    assert category.description == "Разная одежда"
    assert category.products == []


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
    assert len(category1.products) == 2
    assert len(category2.products) == 1
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
