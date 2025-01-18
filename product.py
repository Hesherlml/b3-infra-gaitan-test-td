# product.py

class Product:
    def __init__(self, name: str, price: float, stock: int):
        self.name = name
        self.price = price
        self.stock = stock


    def reduce_stock(self, quantity: int):
        if quantity > self.stock:
            raise ValueError(f"Insufficient stock for {self.name}. Available: {self.stock}")
        self.stock -= quantity
    
    
    def increase_stock(self, quantity: int):
        if quantity < 0:
            raise ValueError("Quantity to increase cannot be negative.")
        self.stock += quantity

    def __str__(self):
        return f"{self.name} ({self.price}€, Stock: {self.stock})"
