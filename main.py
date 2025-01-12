class Product:
    def __init__(self, name, price, quantity):
        """   
        Initialize a product with a name, price, and quantity
        """
        self.name = name 
        self.price = price
        self.quantity = quantity

    def update_quantity(self, amount): 
        """ Update Quantity of product """
    
        self.quantity += amount
        
    def __str__(self):
        """ Return a string representation of the product. """
        
        return f"Product: {self.name}, Price: ${self.price}, Quantity: {self.quantity}"
    
class Inventory:
    def __init__(self):
        """ Initialize Empty inventory """
        
        self.products = {}
        
    def add_product(self, product):
        """ Add product """
        if product.name in self.products:
            self.products[product.name].update_quantity(product.quantity)
        else:
            self.products[product.name] = product
    
    def remove_product(self,product_name):
        """ Remove a product from inventory """
    if product_name in  self.products:
        del self.products[product_name]
    else:
        print(f"Product {product_name} not found")
    
    def sell_product(self, product_name, quantity):
        """ Sell a product to reduce quantity """
        if product_name in self.products:
            product = self.products[product_name]
            if product.quantity >= quantity:
                product.update_quantity(-quantity)
                print(f"Sold {quantity} of {product_name}")
                return product.price * quantity
            else:
                print(f"Insufficient stock for {product_name}")
        else:
            print(f"Product '{product_name}' not found")
        return 0
    
    
    def show_inventory(self):
        """ Display Inventory """
        
        if self.products:
            print("Current Inventory")
            for product in self.products.values():
                print(product)
        else:
            print("Inventory is empty")