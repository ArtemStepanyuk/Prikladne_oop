from .check import Check
from .printable import Printable

class PaperCheck(Check, Printable):
    def __init__(self, amount, products):
        super().__init__(amount, products)

    def display_check(self):
        super().display_check()
        print("Чек буде надруковано на принтері.\n")
