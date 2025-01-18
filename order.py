from cart import Cart

class Order:
    history = []  # Historique des commandes
    def __init__(self, cart):
        self.cart = cart
        self.status = "Pending"  # Le statut initial
        self.total = cart.calculate_total()

    def place_order(self):
        """Place la commande et met à jour le stock"""
        if self.status == "Pending":  # Seules les commandes en attente peuvent être placées
            for product, quantity in self.cart.items.items():  # Accéder correctement à items
                product.stock -= quantity  # Réduit le stock
            self.status = "Completed"
            Order.history.append(self)  # Ajoute la commande à l'historique
            return f"Order placed successfully! Total: {self.total:.2f}€"  # Afficher avec 2 décimales
        else:
            raise ValueError("Order already processed.")

    def cancel_order(self):
        """Annule la commande et restaure le stock"""
        if self.status == "Completed":
            for product, quantity in self.cart.items.items():
                product.stock += quantity  # Restaurer le stock
            self.status = "Cancelled"
        else:
            raise ValueError("Order cannot be cancelled, status is not 'Completed'.")
        
    def reduce_stock(self, quantity):
        if self.stock < quantity:
            raise ValueError(f"Insufficient stock for {self.name}. Available: {self.stock}")
        self.stock -= quantity

    def view_order(self):
        """Affiche les produits et le total de la commande"""
        items_list = "\n".join([f"{product.name} x {quantity}" for product, quantity in self.cart.items.items()])
        return f"{items_list}\nTotal: {self.total:.2f}€"  # Affichage du total avec 2 décimales
