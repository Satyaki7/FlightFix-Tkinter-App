from tkinter import messagebox
import sqlite3
import pandas as pd

def add_city_and_flights(city, flight1, flight2, flight3, flight4, flight5):
    # Check if any input is empty
    if not city or not flight1 or not flight2 or not flight3 or not flight4 or not flight5:
        print("Error: All fields are required.")
        return

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    try:
        # Insert the data into the cities table
        cursor.execute('''
            INSERT INTO cities (CITY, FLIGHT1, FLIGHT2, FLIGHT3, FLIGHT4, FLIGHT5)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (city, flight1, flight2, flight3, flight4, flight5))

        conn.commit()
        print("City and flights added successfully.")
    except sqlite3.IntegrityError as e:
        print(f"Error: {e}")
    finally:
        conn.close()

# Example usage of the function
def view_database():
    conn = sqlite3.connect('users.db')

    # View all data from the users table
    print("Users Table:")
    users_df = pd.read_sql_query("SELECT * FROM users", conn)
    print(users_df.to_string(index=False))
    print("\n")

    # View all data from the cities table
    print("Cities Table:")
    cities_df = pd.read_sql_query("SELECT * FROM cities", conn)
    print(cities_df.to_string(index=False))
    print("\n")

    conn.close()


# Call the function to view the users table

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

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS cities (
        CITY TEXT PRIMARY KEY,
        FLIGHT1 TEXT,
        FLIGHT2 TEXT,
        FLIGHT3 TEXT,
        FLIGHT4 TEXT,
        FLIGHT5 TEXT
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
    view_database()
    
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
def searchfli(city_name):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Convert city_name to lowercase for case-insensitive comparison
    city_name_lower = city_name.lower()

    # Query to retrieve flights for the given city (case-insensitive)
    cursor.execute('SELECT FLIGHT1, FLIGHT2, FLIGHT3, FLIGHT4, FLIGHT5 FROM cities WHERE LOWER(CITY) = ?', (city_name_lower,))
    flights = cursor.fetchone()

    conn.close()

    if flights:
        return flights
    else:
        return None
# Initialize the database and print the tables
initialop()
