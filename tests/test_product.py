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
