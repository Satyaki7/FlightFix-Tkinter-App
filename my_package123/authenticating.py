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
def on_login(u, p):
    username = u
    password = p

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
def on_signup(u, p, q):
    username = u
    password = p

    if username == "Username" or password == "Password":
        messagebox.showerror("Error", "Username and password cannot be empty.")
        return
    elif password != q:
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
        # Insert new user into the users table
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
        conn.commit()

        # Create a new table for the user
        user_table_name = f"user_{username}"
        cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {user_table_name} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            flight_number TEXT NOT NULL,
            departure_place TEXT NOT NULL,
            flight_status TEXT NOT NULL
        )
        ''')
        conn.commit()

        messagebox.showinfo("Success", "User signed up successfully and user table created!")
        return True

    conn.close()

# Function to retrieve user flight data as a list
def get_user_flights(username):
    user_table_name = f"user_{username}"
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Retrieve data from the user's table
    cursor.execute(f'SELECT * FROM {user_table_name}')
    flights = cursor.fetchall()

    conn.close()

    return flights

# Function to add flight details to the user's table
def add_flight(username, flight_number, departure_place, flight_status):
    user_table_name = f"user_{username}"
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Check if user table exists (i.e., user exists)
    cursor.execute(f'''
    CREATE TABLE IF NOT EXISTS {user_table_name} (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        flight_number TEXT NOT NULL,
        departure_place TEXT NOT NULL,
        flight_status TEXT NOT NULL
    )
    ''')
    conn.commit()

    # Insert flight details into the user's table
    cursor.execute(f'''
    INSERT INTO {user_table_name} (flight_number, departure_place, flight_status)
    VALUES (?, ?, ?)
    ''', (flight_number, departure_place, flight_status))
    conn.commit()

    conn.close()
    messagebox.showinfo("Success", "Flight details added successfully!")

# Example usage of add_flight function
def example_add_flight(username, flight_number, departure_place, flight_status):
    add_flight(username, flight_number, departure_place, flight_status)
    flights = get_user_flights(username)
    for flight in flights:
        print(f"Flight Number: {flight[1]}, Departure Place: {flight[2]}, Status: {flight[3]}")

# Example initialization and function calls
if __name__ == "__main__":
    initialop()
    # Assume we have some username and password for demo
    demo_username = "john_doe"
    demo_password = "password123"








# from tkinter import messagebox
# import sqlite3

# def initialop():
#     # Connect to the SQLite database (or create it if it doesn't exist)
#     conn = sqlite3.connect('users.db')

#     # Create a cursor object
#     cursor = conn.cursor()

#     # Create the users table
#     cursor.execute('''
#     CREATE TABLE IF NOT EXISTS users (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         username TEXT NOT NULL UNIQUE,
#         password TEXT NOT NULL
#     )
#     ''')

#     # Commit the changes and close the connection
#     conn.commit()
#     conn.close()

#     print("Database setup complete.")


# # Function to authenticate the user just checking the login info

# def authenticate(username, password):
#     conn = sqlite3.connect('users.db')
#     cursor = conn.cursor()

#     # Check if username exists
#     cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
#     user = cursor.fetchone()

#     # If username does not exist
#     if user is None:
#         conn.close()
#         return "user_not_found"

#     # If username exists, check password
#     cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
#     user = cursor.fetchone()
#     conn.close()

#     if user:
#         return "authenticated"
#     else:
#         return "incorrect_password"

# # Function to handle sign-in button click
# def on_login(u,p):
#     username = u
#     password = p

#     if username == "Username" or password == "Password":
#         messagebox.showerror("Error", "Username and password cannot be empty.")
#         return
    
#     auth_result = authenticate(username, password)

#     if auth_result == "authenticated":
#         messagebox.showinfo("Success", "Signed in successfully!")
#         return True
    
#     elif auth_result == "user_not_found":
#         messagebox.showerror("Error", "User does not exist.")
#     elif auth_result == "incorrect_password":
#         messagebox.showerror("Error", "Incorrect password.")

# # Function to handle sign-up button click
# def on_signup(u,p,q):
#     username = u
#     password = p

#     if username == "Username" or password == "Password":
#         messagebox.showerror("Error", "Username and password cannot be empty.")
#         return
#     elif password != q :
#         messagebox.showerror("Error","Passwords do not match.")
#         return
#     conn = sqlite3.connect('users.db')
#     cursor = conn.cursor()

#     # Check if username already exists
#     cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
#     user = cursor.fetchone()
    
#     if user:
#         messagebox.showerror("Error", "Username already exists.")
#     else:
#         cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
#         conn.commit()
#         messagebox.showinfo("Success", "User signed up successfully!")
#         return True

#     conn.close()


