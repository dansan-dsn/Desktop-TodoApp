import sqlite3

class Todos:
    def __init__(self, user_id, title=None, completed=0, todo_id=None):
        self.user_id = user_id
        self.title = title
        self.completed = completed
        self.todo_id = todo_id
        self.conn = sqlite3.connect('todoApp.db')  # Connection is now an instance attribute
        self.cursor = self.conn.cursor()          # Cursor is now an instance attribute

    def create_todo(self):
        # Insert a new task associated with a specific user
        try:
            self.cursor.execute('''
                INSERT INTO todos (user_id, title, completed)
                VALUES (?, ?, ?)
            ''', (self.user_id, self.title, self.completed))
            self.conn.commit()
            print("Todo created successfully!")
        except Exception as e:
            print(f"Error creating todo: {e}")
        finally:
            self.conn.close()

    def update_todo(self, todo_id, title=None, completed=None):
        # Update the title or completion status of a specific task
        try:
            if title:
                self.cursor.execute('UPDATE todos SET title = ? WHERE id = ?', (title, todo_id))
            if completed is not None:
                self.cursor.execute('UPDATE todos SET completed = ? WHERE id = ?', (completed, todo_id))
            self.conn.commit()
            print("Todo updated successfully!")
        except Exception as e:
            print(f"Error updating todo: {e}")
        finally:
            self.conn.close()

    def delete_todo(self, todo_id):
        # Delete a specific task
        try:
            self.cursor.execute('DELETE FROM todos WHERE id = ?', (todo_id,))
            self.conn.commit()
            print("Todo deleted successfully!")
        except Exception as e:
            print(f"Error deleting todo: {e}")
        finally:
            self.conn.close()

    @staticmethod
    def get_all_todos(user_id):
        # Retrieve all tasks for a specific user
        try:
            conn = sqlite3.connect('todoApp.db')
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM todos WHERE user_id = ?', (user_id,))
            todos = cursor.fetchall()
            conn.close()
            return todos
        except Exception as e:
            print(f"Error fetching todos: {e}")
            return []

    @staticmethod
    def get_one_todo(todo_id):
        # Retrieve a single todo item by its ID
        try:
            conn = sqlite3.connect('todoApp.db')
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM todos WHERE id = ?', (todo_id,))
            todo = cursor.fetchone()
            conn.close()
            return todo
        except Exception as e:
            print(f"Error fetching todo: {e}")
            return None


# CLI for managing todos
def main():
    print('1. Add todo\n2. Update todo\n3. Delete todo\n4. View todos')
    choice = input('Choose an option (1-4): ')

    if choice == '1':
        user_id = int(input('Enter user ID: '))
        title = input('Enter title: ')
        todos = Todos(user_id, title)
        todos.create_todo()

    elif choice == '2':
        todo_id = int(input('Enter todo ID: '))
        title = input('Enter new title (leave blank to keep unchanged): ')
        completed = input('Enter new completed status (0 or 1, leave blank to keep unchanged): ')

        todos = Todos(user_id=None)
        todos.update_todo(
            todo_id,
            title=title if title else None,
            completed=int(completed) if completed else None
        )

    elif choice == '3':
        todo_id = int(input('Enter todo ID: '))
        todos = Todos(user_id=None)
        todos.delete_todo(todo_id)

    elif choice == '4':
        user_id = int(input('Enter user ID: '))
        todos = Todos.get_all_todos(user_id)
        print(f"Todos for user {user_id}:")
        for todo in todos:
            print(todo)

    else:
        print("Invalid choice. Please choose between 1-4.")


if __name__ == '__main__':
    main()
