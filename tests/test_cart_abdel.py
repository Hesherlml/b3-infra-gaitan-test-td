import unittest
from product import Product
from cart import Cart

class TestCart(unittest.TestCase):

    def setUp(self):
        # Initialisation des produits et du panier pour chaque test
        self.p1 = Product(name="Laptop", price=1200.0, stock=10)  # Stock suffisant
        self.p2 = Product(name="Headphones", price=150.0, stock=3)     # Stock faible
        self.p3 = Product(name="Mouse", price=25.0, stock=1)  # Stock très faible
        self.cart = Cart()
        print("\n[Setup] Création des produits et du panier pour les tests.")
        
    def test_notify_low_stock_empty_cart(self):
       #"""Teste si notify_low_stock retourne le bon message pour un panier vide."""
       # Appel de la méthode notify_low_stock sur un panier vide
        notification = self.cart.notify_low_stock()

        # Résultat attendu
        expected_notification = "Tous les produits ont un stock suffisant"

        # Vérification
        self.assertEqual(notification, expected_notification)
        print(f"[Test] Résultat de notify_low_stock pour un panier vide:\n{notification}")

    def test_notify_low_stock(self):
        
        # Ajouter des produits au panier
        self.cart.add_product(self.p1, 1)  # Stock : 10 (non faible)
        self.cart.add_product(self.p2, 1)  # Stock : 3 (faible)
        self.cart.add_product(self.p3, 1)  # Stock : 1 (faible)

        # Appel de la méthode notify_low_stock
        notification = self.cart.notify_low_stock()

        # Résultats attendus
        expected_notification = (
            "Avertissement : stock faible:\n"
            "Headphones (Seulement 3 restants)\n"
            "Mouse (Seulement 1 restants)"
        )

        # Vérification
        self.assertEqual(notification, expected_notification)
        print(f"[Test] Résultat de notify_low_stock :\n{notification}")

    def test_notify_low_stock_no_low_stock(self):
        """Tester si notify_low_stock retourne le bon message quand aucun produit n'a un stock faible."""
        # Ajouter uniquement des produits avec un stock suffisant
        self.cart.add_product(self.p1, 1)  # Stock : 10

        # Appel de la méthode notify_low_stock
        notification = self.cart.notify_low_stock()

        # Réslt attendu
        expected_notification = "Tous les produits ont un stock suffisant"

        # Vérification
        self.assertEqual(notification, expected_notification)
        print(f"[Test] Résultat de notify_low_stock :\n{notification}")
 
if __name__ == "__main__":
    unittest.main(buffer=False)  