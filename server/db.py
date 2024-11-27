# db connection and helper function
import sqlite3

conn = sqlite3.connect('todoApp.db')
cursor = conn.cursor()

def user_model():
     cursor.execute('''
     CREATE TABLE IF NOT EXISTS users (
         id INTEGER PRIMARY KEY AUTOINCREMENT,
         username TEXT UNIQUE NOT NULL,
         password TEXT NOT NULL,
         created_at TEXT DEFAULT CURRENT_TIMESTAMP
     );
     ''')

     conn.commit()
     conn.close()

def todo_model():
     cursor.execute('''
     CREATE TABLE IF NOT EXISTS todos (
         id INTEGER PRIMARY KEY AUTOINCREMENT,
         user_id INTEGER NOT NULL,
         title TEXT NOT NULL,
         completed BOOLEAN NOT NULL DEFAULT 0,
         created_at TEXT DEFAULT CURRENT_TIMESTAMP,
         FOREIGN KEY (user_id) REFERENCES users(id)
     );
     ''')

     conn.commit()
     conn.close()

user_model()
todo_model()