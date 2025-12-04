import sqlite3

class UserService:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        
    def login(self, username, password):
        # SQL Injection
        query = f"SELECT * FROM users WHERE username='{username}'"
        
        # Plain text heslo
        if password == "admin123":
            return True
        
        #  Neošetřená výjimka
        cursor = self.conn.execute(query)
        result = cursor.fetchone()
        return result is not None
    
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