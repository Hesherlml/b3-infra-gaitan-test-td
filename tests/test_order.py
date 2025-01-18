import unittest
from cart import Cart
from product import Product
from order import Order

class TestOrder(unittest.TestCase):
    def setUp(self):
        # Préparation des objets Cart et Product
        self.p1 = Product(name="Laptop", price=1200.0, stock=10)
        self.p2 = Product(name="Headphones", price=150.0, stock=3)
        self.cart = Cart()
        self.cart.add_product(self.p1, 2)
        self.cart.add_product(self.p2, 1)
        self.order = Order(self.cart)
        print("Configuration des tests terminée. Le panier et les produits sont initialisés.")
        
    def test_place_order(self):
        # Tester la méthode place_order
        print("Exécution du test 'test_place_order'...")
        result = self.order.place_order()
        print(f"Résultat de la commande : {result}")
        self.assertEqual(result, "Order placed successfully! Total: 2550.00€")
        print("Stock après la commande :")
        print(f"Produit 1 stock : {self.p1.stock}, Produit 2 stock : {self.p2.stock}")
        self.assertEqual(self.p1.stock, 8)  # Vérifie que le stock a été mis à jour
        self.assertEqual(self.p2.stock, 2)

    def test_cancel_order(self):
        # Tester la méthode cancel_order
        print("Exécution du test 'test_cancel_order'...")
        self.order.place_order()  # Placer la commande avant d'essayer de l'annuler
        print("Commande passée, maintenant on annule...")
        self.order.cancel_order()
        print("Stock après l'annulation de la commande :")
        print(f"Produit 1 stock : {self.p1.stock}, Produit 2 stock : {self.p2.stock}")
        self.assertEqual(self.p1.stock, 10)  # Vérifie que le stock est restauré
        self.assertEqual(self.p2.stock, 3)
        self.assertEqual(self.order.status, "Cancelled")

    def test_order_status(self):
        # Tester le changement de statut
        print("Exécution du test 'test_order_status'...")
        print(f"Statut initial : {self.order.status}")
        self.assertEqual(self.order.status, "Pending")  # Par défaut
        self.order.place_order()
        print(f"Statut après avoir passé la commande : {self.order.status}")
        self.assertEqual(self.order.status, "Completed")

    def test_view_order(self):
        # Tester la méthode view_order
        print("Exécution du test 'test_view_order'...")
        expected_output = "Laptop x 2\nHeadphones x 1\nTotal: 2550.00€"
        actual_output = self.order.view_order()
        print(f"Détails de la commande :\n{actual_output}")
        self.assertEqual(actual_output, expected_output)

    def test_order_history(self):
        # Réinitialiser l'historique avant de commencer le test
        print("Exécution du test 'test_order_history'...")
        Order.history = []  # Réinitialiser l'historique
        history = Order.history
        print(f"Histoire des commandes avant de passer la commande : {history}")
        self.assertEqual(len(history), 0)  # Vérifie que l'historique est vide
        self.order.place_order()
        print(f"Histoire des commandes après avoir passé la commande : {Order.history}")
        self.assertEqual(len(history), 1)  # Vérifie que l'historique a été mis à jour
        self.assertEqual(history[0].total, 2550.00)  # Vérifie que la commande a été ajoutée correctement


if __name__ == "__main__":
    unittest.main()
