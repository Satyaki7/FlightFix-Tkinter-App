from tkinter import messagebox
import sqlite3

def initialop():
    # Connect to the SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect('users.db')

    # Create a cursor object
    cursor = conn.cursor()

    # Create the users table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    )
    ''')

    # Execute a query to list all tables
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

    # Fetch and print the results
    tables = cursor.fetchall()
    for table in tables:
        print(table)

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

    print("Database setup complete.")

# Function to authenticate the user just checking the login info
def authenticate(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Check if username exists
    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    user = cursor.fetchone()

    # If username does not exist
    if user is None:
        conn.close()
        return "user_not_found"

    # If username exists, check password
    cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
    user = cursor.fetchone()
    conn.close()

    if user:
        return "authenticated"
    else:
        return "incorrect_password"

# Function to handle sign-in button click
def on_login(username, password):
    if username == "Username" or password == "Password":
        messagebox.showerror("Error", "Username and password cannot be empty.")
        return

    auth_result = authenticate(username, password)

    if auth_result == "authenticated":
        messagebox.showinfo("Success", "Signed in successfully!")
        return True
    elif auth_result == "user_not_found":
        messagebox.showerror("Error", "User does not exist.")
    elif auth_result == "incorrect_password":
        messagebox.showerror("Error", "Incorrect password.")

# Function to handle sign-up button click
def on_signup(username, password, confirm_password):
    if username == "Username" or password == "Password":
        messagebox.showerror("Error", "Username and password cannot be empty.")
        return
    elif password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match.")
        return

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Check if username already exists
    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    user = cursor.fetchone()

    if user:
        messagebox.showerror("Error", "Username already exists.")
    else:
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
        conn.commit()
        messagebox.showinfo("Success", "User signed up successfully!")
        return True

    conn.close()

# Initialize the database and print the tables
initialop()
