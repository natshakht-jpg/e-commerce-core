from abc import ABC, abstractmethod


class BaseContainer(ABC):
    """Абстрактный базовый класс для контейнеров товаров."""

    @abstractmethod
    def add_product(self, product):  # pragma: no cover
        """Добавить товар в контейнер."""
        pass

    @abstractmethod
    def total_quantity(self):  # pragma: no cover
        """Вернуть общее количество товаров в контейнере."""
        pass

    @abstractmethod
    def total_price(self):  # pragma: no cover
        """Вернуть итоговую стоимость всех товаров в контейнере."""
        pass
