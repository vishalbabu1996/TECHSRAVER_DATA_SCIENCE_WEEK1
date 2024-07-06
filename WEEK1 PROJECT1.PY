import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        min_digits = int(min_digits_entry.get())
        min_uppercase = int(min_uppercase_entry.get())
        min_special = int(min_special_entry.get())

        if length <= 0:
            raise ValueError("Length must be a positive integer.")
        if min_digits + min_uppercase + min_special > length:
            raise ValueError("Minimum character requirements exceed the total length.")

    except ValueError as e:
        messagebox.showerror("Invalid Input", str(e))
        return

    characters = string.ascii_lowercase
    if include_uppercase.get():
        characters += string.ascii_uppercase
    if include_digits.get():
        characters += string.digits
    if include_special.get():
        characters += string.punctuation

    if not characters:
        messagebox.showerror("Invalid Input", "No character set selected.")
        return

    password = []
    if include_digits.get():
        password += random.choices(string.digits, k=min_digits)
    if include_uppercase.get():
        password += random.choices(string.ascii_uppercase, k=min_uppercase)
    if include_special.get():
        password += random.choices(string.punctuation, k=min_special)

    remaining_length = length - len(password)
    password += random.choices(characters, k=remaining_length)
    random.shuffle(password)
    
    password_entry.delete(0, tk.END)
    password_entry.insert(0, ''.join(password))

def copy_to_clipboard():
    window.clipboard_clear()
    window.clipboard_append(password_entry.get())
    messagebox.showinfo("Copied", "Password copied to clipboard.")

# Set up the main window
window = tk.Tk()
window.title("Password Generator")

# Length input
tk.Label(window, text="Password Length:").grid(row=0, column=0, sticky='w')
length_entry = tk.Entry(window)
length_entry.grid(row=0, column=1)

# Include options
include_uppercase = tk.BooleanVar(value=True)
include_digits = tk.BooleanVar(value=True)
include_special = tk.BooleanVar(value=True)

tk.Checkbutton(window, text="Include Uppercase Letters", variable=include_uppercase).grid(row=1, column=0, columnspan=2, sticky='w')
tk.Checkbutton(window, text="Include Digits", variable=include_digits).grid(row=2, column=0, columnspan=2, sticky='w')
tk.Checkbutton(window, text="Include Special Characters", variable=include_special).grid(row=3, column=0, columnspan=2, sticky='w')

# Minimum counts
tk.Label(window, text="Minimum Digits:").grid(row=4, column=0, sticky='w')
min_digits_entry = tk.Entry(window)
min_digits_entry.grid(row=4, column=1)
min_digits_entry.insert(0, "0")

tk.Label(window, text="Minimum Uppercase Letters:").grid(row=5, column=0, sticky='w')
min_uppercase_entry = tk.Entry(window)
min_uppercase_entry.grid(row=5, column=1)
min_uppercase_entry.insert(0, "0")

tk.Label(window, text="Minimum Special Characters:").grid(row=6, column=0, sticky='w')
min_special_entry = tk.Entry(window)
min_special_entry.grid(row=6, column=1)
min_special_entry.insert(0, "0")

# Generate button
generate_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_button.grid(row=7, column=0, columnspan=2)

# Password display
tk.Label(window, text="Generated Password:").grid(row=8, column=0, sticky='w')
password_entry = tk.Entry(window, width=50)
password_entry.grid(row=8, column=1)

# Copy to clipboard button
copy_button = tk.Button(window, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.grid(row=9, column=0, columnspan=2)

# Run the application
window.mainloop()