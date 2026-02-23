from src.product import Product


def test_product_initialization():
    name = "Кроссовки"
    description = "Спортивная обувь"
    price = 5000.50
    quantity = 10

    product = Product(name, description, price, quantity)

    assert product.name == "Кроссовки"
    assert product.description == "Спортивная обувь"
    assert product.price == 5000.50
    assert product.quantity == 10


def test_new_product_without_duplicates():
    """Тест создания нового продукта, если дубликатов нет"""
    products_list = []  # пустой список существующих

    data = {
        "name": "Ноутбук",
        "description": "Мощный ноутбук",
        "price": 50000.0,
        "quantity": 5
    }

    product = Product.new_product(data, products_list)

    assert product.name == "Ноутбук"
    assert product.description == "Мощный ноутбук"
    assert product.price == 50000.0
    assert product.quantity == 5


def test_new_product_with_duplicates():
    """Тест обновления существующего продукта при дубликате"""
    # Создаём существующий продукт
    existing = Product("Ноутбук", "Старый ноутбук", 45000.0, 3)
    products_list = [existing]

    data = {
        "name": "Ноутбук",  # то же имя
        "description": "Новый ноутбук",  # описание игнорируется
        "price": 50000.0,  # цена выше
        "quantity": 2  # количество добавится
    }

    result = Product.new_product(data, products_list)

    # Должен вернуться тот же объект (обновлённый)
    assert result is existing
    assert result.quantity == 5  # 3 + 2
    assert result.price == 50000.0  # взяли более высокую цену
    # Описание не должно измениться
    assert result.description == "Старый ноутбук"


def test_price_getter():
    """Тест геттера цены"""
    product = Product("Тест", "Описание", 1000.0, 10)
    assert product.price == 1000.0


def test_price_setter_positive():
    """Тест установки положительной цены"""
    product = Product("Тест", "Описание", 1000.0, 10)
    product.price = 2000.0
    assert product.price == 2000.0


def test_price_setter_negative():
    """Тест установки отрицательной цены"""
    product = Product("Тест", "Описание", 1000.0, 10)
    product.price = -500  # должно проигнорироваться
    assert product.price == 1000.0  # цена не изменилась


def test_price_setter_decrease_with_confirmation(monkeypatch):
    """Тест понижения цены с подтверждением 'y'"""
    product = Product("Тест", "Описание", 1000.0, 10)

    # Подменяем input, чтобы он возвращал 'y'
    monkeypatch.setattr('builtins.input', lambda _: 'y')

    product.price = 500.0  # понижаем цену
    assert product.price == 500.0  # цена должна измениться


def test_price_setter_decrease_rejected(capsys, monkeypatch):
    """Тест понижения цены с отказом"""
    product = Product("Тест", "Описание", 1000.0, 10)

    # Подменяем input, чтобы он возвращал 'n'
    monkeypatch.setattr('builtins.input', lambda _: 'n')

    product.price = 500.0  # пытаемся понизить
    assert product.price == 1000.0  # цена не изменилась

    # Проверяем, что вывелось сообщение об отмене
    captured = capsys.readouterr()
    assert "Понижение цены отменено" in captured.out


def test_product_str():
    """Тест строкового представления продукта"""
    product = Product("Футболка", "Хлопок", 800, 10)

    expected = "Футболка, 800 руб. Остаток: 10 шт."
    assert str(product) == expected


def test_product_add():
    """Тест сложения продуктов (сумма price * quantity)"""
    p1 = Product("Футболка", "Хлопок", 800, 10)  # 800 * 10 = 8000
    p2 = Product("Джинсы", "Синие", 2500, 5)  # 2500 * 5 = 12500

    result = p1 + p2
    assert result == 8000 + 12500 == 20500
