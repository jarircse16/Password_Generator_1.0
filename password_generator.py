import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random
import string
from datetime import datetime

class PasswordGenerator:
    def __init__(self, window):
        self.window = window
        self.window.title("Password Generator")

        self.label_length = ttk.Label(window, text="Password Length:")
        self.label_length.pack()

        self.entry_length = ttk.Entry(window)
        self.entry_length.pack()

        self.label_types = ttk.Label(window, text="Character Types:")
        self.label_types.pack()

        self.check_uppercase = ttk.Checkbutton(window, text="Uppercase")
        self.check_uppercase.pack()

        self.check_lowercase = ttk.Checkbutton(window, text="Lowercase")
        self.check_lowercase.pack()

        self.check_digits = ttk.Checkbutton(window, text="Digits")
        self.check_digits.pack()

        self.check_special_chars = ttk.Checkbutton(window, text="Special Characters")
        self.check_special_chars.pack()

        self.label_count = ttk.Label(window, text="Number of Passwords to Generate:")
        self.label_count.pack()

        self.entry_count = ttk.Entry(window)
        self.entry_count.pack()

        self.button_generate = ttk.Button(window, text="Generate Passwords", command=self.generate_passwords)
        self.button_generate.pack()

        self.label_result = ttk.Label(window, text="")
        self.label_result.pack()

    def generate_passwords(self):
        length = self.get_password_length()
        types = self.get_character_types()
        count = self.get_password_count()

        if length == 0 or count == 0 or len(types) == 0:
            messagebox.showwarning("Warning", "Please enter valid criteria.")
            return

        passwords = []
        for _ in range(count):
            password = self.generate_password(length, types)
            passwords.append(password)

        self.label_result.config(text="\n".join(passwords))
        self.save_passwords(passwords)

    def get_password_length(self):
        try:
            length = int(self.entry_length.get())
            return length
        except ValueError:
            return 0

    def get_character_types(self):
        types = []
        if self.check_uppercase.instate(['selected']):
            types.append(string.ascii_uppercase)
        if self.check_lowercase.instate(['selected']):
            types.append(string.ascii_lowercase)
        if self.check_digits.instate(['selected']):
            types.append(string.digits)
        if self.check_special_chars.instate(['selected']):
            types.append(string.punctuation)
        return types

    def get_password_count(self):
        try:
            count = int(self.entry_count.get())
            return count
        except ValueError:
            return 0

    def generate_password(self, length, types):
        password = ""
        for _ in range(length):
            char_type = random.choice(types)
            password += random.choice(char_type)
        return password

    def save_passwords(self, passwords):
        current_datetime = datetime.now()
        file_name = current_datetime.strftime("%Y-%m-%d_%H-%M-%S_passwords.txt")
        with open(file_name, "w") as file:
            for password in passwords:
                file.write(password + "\n")
        messagebox.showinfo("Info", f"Passwords saved in {file_name}")

# Create the main window
window = tk.Tk()

# Create a PasswordGenerator instance
generator = PasswordGenerator(window)

# Start the main event loop
window.mainloop()
