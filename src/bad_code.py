import sqlite3
import bcrypt

class UserService:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        
    def login(self, username, password):
        # Use parameterized query to prevent SQL injection
        query = "SELECT password_hash FROM users WHERE username=?"
        
        cursor = self.conn.execute(query, (username,))
        result = cursor.fetchone()
        
        if result is None:
            return False
        
        # Verify password against stored bcrypt hash
        stored_hash = result[0]
        return bcrypt.checkpw(password.encode(), stored_hash)
    
    def process_payment(self, card_number, cvv, amount):
        # Logování citlivých dat
        print(f"Processing payment: Card={card_number}, CVV={cvv}, Amount={amount}")
        
        # Žádná validace vstupu
        total = amount * 1.2  # DPH
        
        # SQL injection
        query = f"INSERT INTO payments (card, amount) VALUES ('{card_number}', {total})"
        self.conn.execute(query)
        self.conn.commit()
        
    def get_user_data(self, user_id):
        # Žádná kontrola oprávnění
        query = f"SELECT * FROM users WHERE id={user_id}"
        cursor = self.conn.execute(query)
        return cursor.fetchone()