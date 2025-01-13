from kivy.app import App 
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.label import Label 
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

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

# --------------- UI LAYOUT ------------------------

class InventoryScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        
        #Product name input
        self.add_widget(Label(text="Prodcuct Name:"))
        self.product_name_input = TextInput(hint_text="Enter product name")
        self.add_widget(self.product_name_input)
        
        #Product price input
        self.add_widget(Label(text="Product Price:"))
        self.product_price_input = TextInput(hint_text="Enter product price")
        self.add_widget(self.product_price_input)
        
        #Product quantity input
        self.add_widget(Label(text="Product Quantity:"))
        self.product_quantity_input = TextInput(hint_text="Enter product quantity")
        self.add_widget(self.product_quantity_input)
        
        #Add product button
        self.add_button  = Button(text="Add product", size_hint=(1, 0.5))
        self.add_button.bind(on_press=self.add_product)
        self.add_widget(self.add_button)
        
        #Show inventory
        self.show_inventory_button = Button(text="Show Inventory", size_hint=(1, 0.5))
        self.show_inventory_button.bind(on_press=self.show_inventory)
        self.add_widget(self.show_inventory_button)
        
        #Display Area
        self.result_label = Label(text="")
        self.add_widget(self.result_label)
        
        #Inventory dictionary
        
        self.inventory = {}
        
    def add_product(self, instance):
        #Get input values
        name = self.product_name_input.text
        price = self.product_price_input.text
        quantity = self.product_quantity_input.text
        
        if name and price and quantity:
            #Add product
            self.inventory[name] = {
                'price': float(price),
                'quantity': int(quantity)
            }
            self.result_label.text = f"Added {name} to inventory!"
            
            self.product_name_input.text = ""
            self.product_price_input.text = ""
            self.product_quantity_input.text = ""
            
        else:
            self.result_label.text = "Please complete all fields"
    
    def show_inventory(self,instance):
        if self.inventory:
            inventory_text = "Current Inventory:\n"
            for name, details in self.inventory.items():
                inventory_text = f"{name}: ${details['price']}, Quantity:{details['quantity']}\n"
            self.result_label.text = inventory_text
        else:
            self.result_label.text = "Inventory is empty"
class InventoryApp(App):
    def build(self):
        return InventoryScreen()

if __name__ == "__main__":
    InventoryApp().run()
