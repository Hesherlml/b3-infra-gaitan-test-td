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

    def remise_produit(self):
        total_sans_remise = sum(product.price * quantity for product, quantity in self.items.items())

        total_quantite = sum(quantity for product, quantity in self.items.items())

        if 10 < total_quantite <= 15:
            
            total_remise = total_sans_remise * 0.10
            
            total_avec_remise = total_sans_remise - total_remise
            
            return f"Votre remise est de '10%' et votre total est de {total_avec_remise}"
        elif total_quantite > 15:
        
            total_remise = total_sans_remise * 0.20
        
            total_avec_remise = total_sans_remise - total_remise
        
            return f"Votre remise est de '20%' et votre total est de {total_avec_remise}"
        else:
            # Sans remise
            return f"Vous n'avez pas de remise et votre total est de {total_sans_remise}"