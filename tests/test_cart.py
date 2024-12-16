


# import unittest
# from cart import Cart
# from product import Product

# class TestCart(unittest.TestCase):

#     def setUp(self):
#         """Initialisation des objets pour les tests."""
#         self.cart = Cart()
#         self.product1 = Product("Product 1", 20.0, 10)  # Nom, prix, stock
#         self.product2 = Product("Product 2", 50.0, 5)

#         # Ajouter des produits au panier
#         self.cart.add_product(self.product1, 2)  # 2 x 20 = 40
#         self.cart.add_product(self.product2, 1)  # 1 x 50 = 50

#     def test_apply_valid_discount_code(self):
#         """Test de l'application d'un code promo valide."""
#         total_before_discount = self.cart.calculate_total()
#         total_after_discount = self.cart.apply_discount_code("SAVE10")
        
#         # Vérifications
#         self.assertEqual(total_before_discount, 90.0, "Le total avant réduction est incorrect.")
#         self.assertEqual(total_after_discount, 81.0, "La réduction de 10% n'a pas été appliquée correctement.")

#     def test_apply_another_valid_discount_code(self):
#         """Test de l'application d'un autre code promo valide."""
#         total_after_discount = self.cart.apply_discount_code("SAVE20")
        
#         # Vérifications
#         self.assertEqual(total_after_discount, 72.0, "La réduction de 20% n'a pas été appliquée correctement.")

#     def test_apply_invalid_discount_code(self):
#         """Test de l'application d'un code promo invalide."""
#         with self.assertRaises(ValueError) as context:
#             self.cart.apply_discount_code("INVALID_CODE")

#         # Vérification du message d'erreur
#         self.assertEqual(str(context.exception), "Invalid discount code: INVALID_CODE.")

#     def test_no_discount_code(self):
#         """Test sans code promo : le total doit rester inchangé."""
#         total = self.cart.calculate_total()
#         self.assertEqual(total, 90.0, "Le total sans code promo est incorrect.")

# if __name__ == "__main__":
#     unittest.main()

    