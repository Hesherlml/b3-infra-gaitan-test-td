# cart.py

from product import Product

class Cart:
    def __init__(self):
        self.items = {}  # {product: quantity}

    def add_product(self, product: Product, quantity: int):
        if product.stock < quantity:
            raise ValueError(f"Cannot add {quantity} of {product.name}. Only {product.stock} left.")
        self.items[product] = self.items.get(product, 0) + quantity

    def remove_product(self, product: Product):
        if product in self.items:
            del self.items[product]
        else:
            raise KeyError(f"{product.name} is not in the cart.")

    def calculate_total(self):
        return sum(product.price * quantity for product, quantity in self.items.items())

    def display_cart(self):
        if not self.items:
            return "Your cart is empty."
        return "\n".join([f"{product.name} x {quantity} - {product.price * quantity}€"
                          for product, quantity in self.items.items()])
    

    def apply_discount_code(self, code: str):
        discount_codes = {"SAVE10": 10, "SAVE20": 20}  # Exemple : 10% ou 20% de réduction
        if code not in discount_codes:
            raise ValueError(f"Invalid discount code: {code}.")
        discount = discount_codes[code]
        total = self.calculate_total()
        return total * (1 - discount / 100)

