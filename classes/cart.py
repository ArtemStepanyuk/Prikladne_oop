class Cart:
    def __init__(self):
        self.products = [] 
        self.__discount = 0 

    def add_product(self, product, quantity=1):
        for idx, (prod, qty) in enumerate(self.products):
            if prod.name == product.name:
                self.products[idx] = (prod, qty + quantity)
                print(f"Додано {quantity} x {product.name} (нове кількість: {qty + quantity}).")
                return
        self.products.append((product, quantity))
        print(f"Додано {quantity} x {product.name} за ціною {product.price} грн. кожен.")

    def remove_product(self, product_name, quantity=1):
        for idx, (prod, qty) in enumerate(self.products):
            if prod.name.lower() == product_name.lower():
                if quantity >= qty:
                    del self.products[idx]
                    print(f"Видалено весь продукт '{prod.name}' з кошика.")
                else:
                    self.products[idx] = (prod, qty - quantity)
                    print(f"Видалено {quantity} x '{prod.name}'. Залишилося: {qty - quantity}.")
                return
        print(f"Продукт '{product_name}' не знайдено у кошику.")

    def calculate_total(self):
        total = sum(product.price * quantity for product, quantity in self.products)
        total -= self.__apply_discount(total)
        return total

    def __apply_discount(self, total):
        if len(self.products) > 3:
            self.__discount = 0.10 * total
            print(f"Застосовано знижку: {self.__discount} грн.")
            return self.__discount
        return 0

    def display_cart(self):
        print("\n=== Ваш кошик ===")
        if not self.products:
            print("Кошик порожній.")
            return
        for product, quantity in self.products:
            print(f"{quantity} x {product.name} - {product.price * quantity} грн.")
        print(f"Всього: {self.calculate_total()} грн.\n")
