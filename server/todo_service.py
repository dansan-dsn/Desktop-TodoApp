# handle crud operations for todo items
import sqlite3

class Todos:
    def __init__(self, title, completed):
        self.title = title
        self.completed = completed
        self.conn = sqlite3.connect('todoApp.db')
        self.cursor = self.conn.cursor()

    def create_todo(self):
        self.cursor.execute('INSERT INTO todoApp (title) VALURES (?)', (self.title))
        self.conn.commit()
        self.conn.close()

    def update_todo(self, title):
        self.cursor.execute('UPDATE todoApp SET title = ? WHERE title = ?', (title, self.title))
        self.conn.commit()
        self.conn.close()