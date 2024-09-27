from classes.product import Product
from classes.cart import Cart
from classes.electronic_check import ElectronicCheck
from classes.paper_check import PaperCheck

def display_products(products):
    print("\n=== Список доступних продуктів ===")
    for idx, product in enumerate(products, start=1):
        print(f"{idx}. {product.name} - {product.price} грн.")

def display_cart_options():
    print("\n=== Опції кошика ===")
    print("1. Додати продукт")
    print("2. Видалити продукт")
    print("3. Завершити вибір продуктів")

def main():
    products = [
        Product("Хліб", 30),
        Product("Молоко", 60),
        Product("Яйця", 70),
        Product("Сир", 150),
        Product("Масло", 120)
    ]

    cart = Cart()

    while True:
        display_products(products)
        display_cart_options()
        try:
            choice = int(input("Виберіть дію (1-3): "))
        except ValueError:
            print("Будь ласка, введіть числове значення.")
            continue

        if choice == 1:
            try:
                product_choice = int(input("Виберіть номер продукту для додавання: "))
                if 1 <= product_choice <= len(products):
                    selected_product = products[product_choice - 1]
                    quantity = int(input(f"Введіть кількість '{selected_product.name}': "))
                    if quantity < 1:
                        print("Кількість має бути позитивним числом.")
                        continue
                    cart.add_product(selected_product, quantity)
                else:
                    print("Некоректний вибір. Спробуйте знову.")
            except ValueError:
                print("Будь ласка, введіть числове значення.")
                continue
        elif choice == 2:
            if not cart.products:
                print("Кошик порожній. Немає продуктів для видалення.")
                continue
            cart.display_cart()
            try:
                product_number = int(input("Введіть номер продукту для видалення: "))
                if 1 <= product_number <= len(products):
                    product_to_remove = products[product_number - 1]
                    product_names_in_cart = [prod.name for prod, _ in cart.products]
                    if product_to_remove.name not in product_names_in_cart:
                        print(f"Продукт '{product_to_remove.name}' не знайдено у кошику.")
                        continue
                    quantity = int(input(f"Введіть кількість '{product_to_remove.name}' для видалення: "))
                    if quantity < 1:
                        print("Кількість має бути позитивним числом.")
                        continue
                    cart.remove_product(product_to_remove.name, quantity)
                else:
                    print("Некоректний номер продукту. Спробуйте знову.")
            except ValueError:
                print("Будь ласка, введіть числове значення.")
                continue
        elif choice == 3:
            break
        else:
            print("Некоректний вибір. Спробуйте знову.")

    if not cart.products:
        print("Ваш кошик порожній. Завершення програми.")
        return

    cart.display_cart()

    print("Виберіть тип чека:")
    print("1. Електронний чек")
    print("2. Паперовий чек")
    while True:
        try:
            check_type = int(input("Введіть 1 або 2: "))
            if check_type not in [1, 2]:
                print("Некоректний вибір. Введіть 1 або 2.")
                continue
            break
        except ValueError:
            print("Будь ласка, введіть числове значення (1 або 2).")

    total_amount = cart.calculate_total()
    products_in_cart = cart.products

    if check_type == 1:
        email = input("Введіть ваш email для відправки чека: ")
        check = ElectronicCheck(total_amount, products_in_cart, email)
    else:
        check = PaperCheck(total_amount, products_in_cart)

    check.display_check()


if __name__ == "__main__":
    main()
