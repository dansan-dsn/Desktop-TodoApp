# gui.py
import tkinter as tk
from tkinter import messagebox
from server.user_auth import User

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Todo App - User Authentication")

        # Username and Password Entry Widgets
        self.username_label = tk.Label(root, text="Username")
        self.username_label.pack()

        self.username_entry = tk.Entry(root)
        self.username_entry.pack()

        self.password_label = tk.Label(root, text="Password")
        self.password_label.pack()

        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.pack()

        # Register and Login Buttons
        self.register_button = tk.Button(root, text="Register", command=self.register_user)
        self.register_button.pack()

        self.login_button = tk.Button(root, text="Login", command=self.login_user)
        self.login_button.pack()

    def register_user(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username and password:
            user = User(username, password)
            result = user.register()
            messagebox.showinfo("Registration", result)
        else:
            messagebox.showwarning("Input Error", "Please enter both username and password.")

    def login_user(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username and password:
            result = User.login(username, password)
            if result == True:
                messagebox.showinfo("Login", "Login successful.")
            else:
                messagebox.showerror("Login", result)
        else:
            messagebox.showwarning("Input Error", "Please enter both username and password.")

# Main Program
if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
