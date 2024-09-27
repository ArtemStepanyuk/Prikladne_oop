class Check:
    def __init__(self, amount, products):
        self.amount = amount     
        self.products = products  

    def display_check(self):
        print(f"\n=== Ваш чек ===")
        print("Список придбаних продуктів:")
        for product, quantity in self.products:
            print(f"- {product.name} x{quantity} = {product.price * quantity} грн.")
        print(f"Сума: {self.amount} грн.\n")
