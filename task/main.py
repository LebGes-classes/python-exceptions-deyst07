"""Главный модуль программы."""


from models import ProductManager
from exceptions import ProductError


def main() -> None:
    """
    Основная функция запуска программы.

    Реализует интерфейс и обработку действий
    пользователя.

    Returns:
        None
    """

    manager = ProductManager()
    is_running = True

    while is_running:
        print("\n☆☆☆☆☆☆ МЕНЮ ☆☆☆☆☆☆")
        print("1 - Создать карточку товара.")
        print("2 - Показать карточку товара.")
        print("3 - Изменить количество товара.")
        print("4 - Изменить состояние товара(списано/создано/в ремонте/принято к учёту).")
        print("5 - Списать товар с учёта.")
        print("6 - Удалить товар.")
        print("0 - ВЫХОД")
        print("☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")

        choice = input("★ВЫБЕРИТЕ ДЕЙСТВИЕ: ")

        try:
            match choice:
                case "1":
                    name = input("\nНаименование: ")
                    category = input("Категория: ")
                    description = input("Описание: ")
                    quantity = int(input("Количество: "))
                    supplier = input("Поставщик: ")
                    manufacturer = input("Производитель: ")
                    price = float(input("Стоимость: "))
                    location = input("Местоположение: ")

                    manager.create_product(
                        name,
                        category,
                        description,
                        quantity,
                        supplier,
                        manufacturer,
                        price,
                        location,
                    )
                    
                    print("Карточка создана.")

                case "2":
                    product_id = int(input("\nВведите ID: "))
                    product = manager.get_product(product_id)
                    
                    if product:
                        product.show_info()
                    else:
                        
                        print("Карточка не найдена.")
            
                case "3":
                    product_id = int(input("\nВведите ID: "))
                    new_quantity = int(input("Введите новое количество товара: "))
                    product = manager.get_product(product_id)
                    
                    if product:
                        product.change_quantity(new_quantity)
                        
                        print("Количество изменено.")
                    else:
                        
                        print("Карточка не найдена.")

                case "4":
                    product_id = int(input("\nВведите ID: "))
                    new_condition = input("Новое состояние: ")
                    product = manager.get_product(product_id)
                    
                    if product:
                        product.change_condition(new_condition)
                        
                        print("Состояние изменено.")
                    else:
                        
                        print("Карточка не найдена.")
            
                case "5":
                    product_id = int(input("\nВведите ID: "))
                    product = manager.get_product(product_id)
                    
                    if product:
                        product.write_off()
                        
                        print("Товар списан.")
                    else:
                        
                        print("Карточка не найдена.")

                case "6":
                    product_id = int(input("\nВведите ID: "))
                    manager.delete_product(product_id)
                    
                    print("Карточка удалена.")

                case "0":
                    is_running = False
                    
                    print("\n!ВыХоД Из пРоГрАмМы!")

                case _:
                    
                    print("Неверный ввод.")
        
        except ProductError as error:
            
            print("Ошибка: ", error)
        
        except ValueError:
            
            print("Ошибка: неверный ввод данных.")

if __name__ == "__main__":
    main()
