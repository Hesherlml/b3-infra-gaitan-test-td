import unittest
from cart import Cart
from product import Product

class TestCart(unittest.TestCase):

    def test_remise(self):
        #Initialisation
        crt = Cart()        
        p2 = Product("Headphones", 150.0, 20)

        # Ajout des produits dans panier
        try:
            crt.add_product(p2,11)
        except ValueError as e:
            print(f"Error: {e}")

        result = crt.remise_produit()
        
        total_sans_remise = 150.0 * 11
        
        total_avec_remise = total_sans_remise - (total_sans_remise * 0.10)  # 10% de Remise
        
        expected_message = f"Votre remise est de '10%' et votre total est de {total_avec_remise}"


        #appel de la fonction
        self.assertEqual(result,expected_message)

if __name__ == "__main__":
    unittest.main(buffer=False)  # Disable buffering to display prints