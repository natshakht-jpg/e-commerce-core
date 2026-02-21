from src.utils import load_from_json


def test_load_from_json():
    categories = load_from_json("data/products.json")

    assert len(categories) == 2
    assert categories[0].name == "Смартфоны"

    # Проверяем первую категорию
    products1 = categories[0].products
    assert "Samsung Galaxy C23 Ultra" in products1
    assert "Iphone 15" in products1
    assert "Xiaomi Redmi Note 11" in products1

    # Проверяем второй продукт в первой категории
    assert "Iphone 15" in products1
    assert "210000.0" in products1
