from .check import Check

class ElectronicCheck(Check):
    def __init__(self, amount, products, email):
        super().__init__(amount, products)
        self.email = email

    def display_check(self):
        super().display_check()
        print(f"Електронний чек відправлено на email: {self.email}\n")
