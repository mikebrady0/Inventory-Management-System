import sqlite3
class InventoryDatabase:
    def __init__(self, db_name="inventory.db"):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()
        
        
    def create_table(self):
        """Create inventory table if it doesnt exist. """
        self.cursor.execute('''
                            CREATE TABLE IF NOT EXISTS inventory (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                name TEXT UNIQUE,
                                price REAL,
                                quantity INTEGER
                            )
                        ''')
        self.connection.commit()
    
    def add_product(self, name, price, quantity):
        """Add a new product to the database """
        try:
            self.cursor.execute('''
                                INSERT INTO inventory (name, price, quantity)
                                VALUES (?, ?, ?)
                                ''', (name, price, quantity))
            self.connection.commit()
            return True
        except sqlite3.IntegrityError:
            return False
        
    def update_product_quantity(self, name, quantity_change):
        """Update quantity of product"""
        self.cursor.execute('''
                            UPDATE inventory
                            SET quantity = quantity + ?
                            WHERE name = ?
                            ''', (quantity_change, name))
        self.connection.commit()
        
    def get_all_products(self):
        """Retrieve products from database"""
        self.cursor.execute('SELECT name, price, quantity FROM inventory')
        return self.cursor.fetchall()
    
    def get_product(self, name):
        """Get product by name"""
        self.cursor.execute('SELECT name, price, quantity FROM inventory WHERE name = ?')
        self.cursor.fetchone()
        
    def delete_product(self, name):
        """Delete a product from the database."""
        self.cursor.execute('DELETE FROM inventory WHERE name = ?', (name,))
        self.connection.commit()
        
    def __del__(self):
        self.connection.close()
        
