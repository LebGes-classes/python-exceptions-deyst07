"""Модели товара и менеджера товаров."""


from exceptions import (
    ProductError,
    InvalidQuantityError,
    InvalidPriceError,
    InvalidConditionError,
    WriteOffError,
)


class ProductCard:
    """Класс карточки товара."""
    
    ALLOWED_CONDITIONS = (
            "списано",
            "создано",
            "в ремонте",
            "принято к учёту",
        )
    
    def __init__ (
            self,
            product_id: int,
            name: str,
            category: str,
            description: str,
            quantity: int,
            condition: str,
            supplier: str,
            manufacturer: str,
            price: float,
            location: str,
    ) -> None:
        """
        Инициализирует объект карточки товара.

        Args:
            product_id (int): Уникальный идентификатор товара.
            name (str): Наименование товара.
            category (str): Категория товара.
            description (str): Описание товара.
            quantity (int): Количество товара.
            condition (str): Состояние товара.
            supplier (str): Поставщик товара.
            manufacturer (str): Производитель товара.
            price (float): Стоимость товара.
            location (str): Местоположение товара.
        
        Returns:
            None
        """
        if quantity < 0:
            raise InvalidQuantityError(
                "Количество не может быть отрицательным."
            )
        
        if price < 0:
            raise InvalidPriceError(
                "Стоимость не может быть отрицательной."
            )

        self.product_id = product_id
        self.name = name
        self.category = category
        self.description = description
        self.quantity = quantity
        self.condition = condition
        self.supplier = supplier
        self.manufacturer = manufacturer
        self.price = price
        self.location = location
    
    def show_info(self) -> None:
        """
        Выводит информацию о товаре.
        
        Returns:
            None
        """

        print("\n☆☆☆ Информация о товаре ☆☆☆")
        print("ID:", self.product_id)
        print("Наименование:", self.name)
        print("Категория:", self.category)
        print("Описание:", self.description)
        print("Количество:", self.quantity)
        print("Состояние:", self.condition)
        print("Поставщик:", self.supplier)
        print("Производитель:", self.manufacturer)
        print("Стоимость:", self.price)
        print("Местоположение:", self.location)
        print("☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")

    def change_quantity(self, new_quantity: int) -> None:
        """
        Изменяет количество товара.
        
        Args:
            mew_quantity (int): Новое количество товара.
        
        Raises:
            InvalidQuantityError: Если количество отрицательное.
        
        Returns:
            None
        """

        if new_quantity < 0:
            raise InvalidQuantityError(
                "Количество не может быть отрицательным!"
            )
        
        self.quantity = new_quantity
    
    def change_condition(self, new_condition: str) -> None:
        """
        Изменяет состояние товара.
        
        Args:
            new_condition (str): Новое состояние товара.

        Raises:
            InvalidConditionError: Если состояние недопустимо
                или товар уже списан.
        
        Returns:
            None
        """

        if new_condition not in self.ALLOWED_CONDITIONS:
            raise InvalidConditionError(
                "Недопустимое состояние товара!"
            )
        
        if self.condition == "списано":
            raise InvalidConditionError(
                "Невозможно изменить состояние списанного товара!"
            )
        
        self.condition = new_condition

    def write_off(self) -> None:
        """
        Списывает товар с учёта.
        
        Raises:
            WriteOffError: Если товар не в состоянии
                "принято к учёту".
        
        Returns:
            None
        """

        if self.condition != "принято к учёту":
            raise WriteOffError(
                "Списание возможно только товара на учёте."
            )
        
        self.condition = "списано"

class ProductManager:
    """Класс для управления карточками товаров."""

    def __init__(self) -> None:
        """
        Инициализурует менеджер товаров.
        
        Создаёт пустой словарь для хранения товаров
        и счётчик(ID) товаров.
        """

        self.products = {}
        self.next_id = 1

    def create_product(
            self,
            name: str,
            category: str,
            description: str,
            quantity: int,
            supplier: str,
            manufacturer: str,
            price: float,
            location: str,
    ) -> None:
        """
        Создаёт новую карточку товара и добавляет в словарь.
        
        Args:
            name (str): Наименование товара.
            category (str): Категория товара.
            description (str): Описание товара.
            quantity (int): Количество товара.
            supplier (str): Поставщик товара.
            manufacturer (str): Производитель товара.
            price (float): Стоимость товара.
            location (str): Местоположение товара.

        Returns:
            None
        """

        product = ProductCard(
            self.next_id,
            name,
            category,
            description,
            quantity,
            "создано",
            supplier,
            manufacturer,
            price,
            location,
        )

        self.products[self.next_id] = product
        self.next_id += 1

    def get_product(self, product_id: int) -> ProductCard | None:
        """
        Возвращает карточку товара по ID.

        Args:
            product_id (int): Идентификатор(ID) товара.

        Returns:
            ProductCard | None: Карточка товара, если найдена,
                иначе None.
        """

        return self.products.get(product_id)
    
    def delete_product(self, product_id: int) -> None:
        """
        Удаляет карточку товара по ID.

        Args:
            product_id (int): Идентификатор(ID) товара.
        
        Raises:
            ProductError: Если товар не найден.

        Returns:
            None
        """

        if product_id not in self.products:
            raise ProductError("Товара с таким ID не существует.")
        
        del self.products[product_id]
