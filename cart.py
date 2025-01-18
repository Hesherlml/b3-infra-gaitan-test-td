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
        
        
############################################## fonction ajouter abdelmounaim EL HOUZI ####################################################
    def notify_low_stock(self):
        # """Avertir l'utilisateur si un produit dans le panier a un stock faible."""
        low_stock_products = [] # stocké le nome des produit qui ont un stock faible
        for product in self.items.keys():
            if product.stock <= 5:  
                low_stock_products.append(f"{product.name} (Seulement {product.stock} restants)")

        if low_stock_products:
            return "Avertissement : stock faible:\n" + "\n".join(low_stock_products)
        return "Tous les produits ont un stock suffisant"
    

    
############################################## fonction ajouter AIT SAID Yahia ####################################################
    def apply_discount_code(self, code: str):
        discount_codes = {"SAVE10": 10, "SAVE20": 20}  # Exemple : 10% ou 20% de réduction
        if code not in discount_codes:
            raise ValueError(f"Invalid discount code: {code}.")
        discount = discount_codes[code]
        total = self.calculate_total()
        return total * (1 - discount / 100)
    
############################################## fonction ajouter GAITAN Gabriel ####################################################  
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



  
if __name__ == "__main__":
    Cart()
    