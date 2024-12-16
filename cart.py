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
    
    def notify_low_stock(self):
        # """Avertir l'utilisateur si un produit dans le panier a un stock faible."""
        low_stock_products = [] # stocké le nome des produit qui ont un stock faible
        for product in self.items.keys():
            if product.stock <= 5:  
                low_stock_products.append(f"{product.name} (Seulement {product.stock} restants)")

        if low_stock_products:
            return "Avertissement : stock faible:\n" + "\n".join(low_stock_products)
        return "Tous les produits ont un stock suffisant"
