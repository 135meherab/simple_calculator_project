import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate a random password
def generate_password():
    length = 12  # Set the desired length of the password
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    password_entry.delete(0, tk.END)  # Clear previous entry
    password_entry.insert(tk.END, password)

# Function to validate login credentials
def login():
    username = username_entry.get()
    password = password_entry.get()
    # Add your validation logic here (e.g., checking against a stored username and password)

    if username == "your_username" and password == "your_password":
        messagebox.showinfo("Success", "Login Successful!")
        # Add code to open the password vault or perform other actions
    else:
        messagebox.showerror("Error", "Invalid username or password!")

# Create the main window
window = tk.Tk()
window.title("Password Vault")

# Create and position login form elements
username_label = tk.Label(window, text="Username:")
username_label.pack()
username_entry = tk.Entry(window)
username_entry.pack()

password_label = tk.Label(window, text="Password:")
password_label.pack()
password_entry = tk.Entry(window, show="*")
password_entry.pack()

login_button = tk.Button(window, text="Login", command=login)
login_button.pack()

# Create and position password generation button
generate_password_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_password_button.pack()

# Start the Tkinter event loop
window.mainloop()
