from src.utils import load_from_json


def test_load_from_json():
    categories = load_from_json("data/products.json")

    assert len(categories) == 2
    assert categories[0].name == "Смартфоны"
    assert len(categories[0].products) == 3
    assert categories[0].products[1].name == "Iphone 15"
    assert categories[0].products[1].price == 210000.0
