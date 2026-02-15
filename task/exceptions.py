"""Модуль пользовательских исключений для товаров."""


class ProductError(Exception):
    """Базовое исключение для операций с товаром."""
    pass


class InvalidQuantityError(ProductError):
    """Ошибка некорректного количества(отрицательное)."""
    pass


class InvalidPriceError(ProductError):
    """Ошибка некорректной стоимости товара."""
    pass


class InvalidConditionError(ProductError):
    """Ошибка недопустимого состояния."""
    pass


class WriteOffError(ProductError):
    """Ошибка списания товара."""
    pass
