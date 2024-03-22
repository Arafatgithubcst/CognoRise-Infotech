import tkinter as tk
from tkinter import messagebox
import string
import random

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        self.label = tk.Label(root, text="Password Length:")
        self.label.grid(row=0, column=0, padx=10, pady=10)

        self.entry = tk.Entry(root)
        self.entry.grid(row=0, column=1, padx=10, pady=10)

        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password)
        self.generate_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        self.password_label = tk.Label(root, text="")
        self.password_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    def generate_password(self):
        try:
            length = int(self.entry.get())
            if length <= 0:
                messagebox.showerror("Error", "Password length should be a positive integer.")
                return
            characters = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(random.choice(characters) for _ in range(length))
            self.password_label.config(text="Generated Password: " + password)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid integer for password length.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
