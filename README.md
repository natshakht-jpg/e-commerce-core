# E-commerce Core

## Описание

Ядро для интернет-магазина. Реализованы базовые классы для работы с товарами и категориями.

## Установка

1. Клонируйте репозиторий
2. Установите зависимости:
```
poetry install
```
## Использование

from src.product import Product
from src.category import Category

### Создание товаров
product1 = Product("Ноутбук", "Мощный ноутбук", 50000.0, 5)
product2 = Product("Мышь", "Беспроводная мышь", 1500.0, 10)

### Создание категории с товарами
category = Category("Электроника", "Товары для дома", [product1, product2])

## Загрузка данных из JSON
В проекте реализована функция `load_from_json` в модуле `utils.py`, которая позволяет загружать категории и товары из JSON-файла.

Пример использования:
```
from src.utils.utils import load_from_json

categories = load_from_json("data/products.json")
```

## Документация

В проекте реализованы:
- Класс Product с атрибутами: name, description, price, quantity
- Класс Category с атрибутами: name, description, products
- Автоматический подсчет количества категорий и товаров

## Лицензия

Этот проект лицензирован по [лицензии MIT] (LICENSE)
