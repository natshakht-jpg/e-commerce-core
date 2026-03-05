class ProductPrintMixin:
    """
    Миксин: выводит информацию о созданном объекте.
    """

    def __init__(self, *args, **kwargs):
        """
        Конструктор миксина. Передаёт аргументы родителю, затем печатает
        repr(self).
        """
        # Передаём аргументы дальше по цепочке наследования
        super().__init__(*args, **kwargs)

        # Печатаем строковое представление уже готового объекта
        print(repr(self))

    def __repr__(self):
        """
        Возвращает строку для печати в формате:
        ИмяКласса(название, описание, цена, количество)
        """
        return f"{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})"
