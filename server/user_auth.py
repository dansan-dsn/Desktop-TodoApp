import bcrypt
import sqlite3

class Users:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def register(self):
        conn = sqlite3.connect('todoApp.db')
        cursor = conn.cursor()

        # Ensure username is passed correctly as a tuple for parameterized query
        cursor.execute('SELECT * FROM users WHERE username = ?', (self.username,))
        existing_user = cursor.fetchone()

        if existing_user:
            print("Username not available.")
        else:
            # Hash the password before storing
            hashed_password = bcrypt.hashpw(self.password.encode('utf-8'), bcrypt.gensalt())
            cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (self.username, hashed_password))
            conn.commit()
            print("User registered successfully.")

        conn.close()

    @staticmethod
    def login(username, password):
        conn = sqlite3.connect('todoApp.db')
        cursor = conn.cursor()

        # Fetch only the password field from the users table
        cursor.execute('SELECT password FROM users WHERE username = ?', (username,))
        user = cursor.fetchone()

        if user:
            # Compare entered password with stored password hash
            if bcrypt.checkpw(password.encode('utf-8'), user[0]):  # user[0] contains the hashed password
                print("Login successful.")
                conn.close()
                return True
            else:
                print("Incorrect password.")
        else:
            print("User not found.")

        conn.close()
        return False


# Main Program
print("1. Register\n2. Login")
choice = input("Choose an option (1 or 2): ")

if choice == '1':
    username = input("Enter username: ")
    password = input("Enter password: ")
    user = Users(username, password)
    user.register()
elif choice == '2':
    username = input("Enter username: ")
    password = input("Enter password: ")
    Users.login(username, password)
else:
    print("Invalid option. Please choose 1 for Register or 2 for Login.")
