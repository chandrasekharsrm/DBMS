import tkinter as tk
from tkinter import messagebox
import mysql.connector
import subprocess

# Connect to MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456789",
    database="legal_link"
)

mycursor = mydb.cursor()

# Function to create table if it doesn't exist
def create_table():
    mycursor.execute("CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255), password VARCHAR(255))")

create_table()

# Function to handle signup
def signup():
    username = signup_username.get()
    password = signup_password.get()

    sql = "INSERT INTO login (user_name, password) VALUES (%s, %s)"
    val = (username, password)
    mycursor.execute(sql, val)
    mydb.commit()

    messagebox.showinfo("Success", "Signup successful!")

# Function to handle login
def login():
    username = login_username.get()
    password = login_password.get()

    sql = "SELECT * FROM login WHERE user_name = %s AND password = %s"
    val = (username, password)
    mycursor.execute(sql, val)
    result = mycursor.fetchone()

    if result:
        messagebox.showinfo("Success", "Login successful!")
        open_welcome_window()
    else:
        messagebox.showerror("Error", "Invalid username or password")


# Function to open welcome window
def open_welcome_window():
    welcome_window = tk.Toplevel(root)
    welcome_window.title("Welcome")

    welcome_label = tk.Label(welcome_window, text="Welcome!")
    welcome_label.pack(pady=10)

    button1 = tk.Button(welcome_window, text="Register Case", command=run_file1)
    button1.pack(pady=5)

    button2 = tk.Button(welcome_window, text="Explore Lawyers", command=run_file2)
    button2.pack(pady=5)

    button2 = tk.Button(welcome_window, text="Ai - Assist", command=run_file3)
    button2.pack(pady=5)
# Function to run file.py
def run_file1():
    subprocess.run(["python", "register.py"])
def run_file2():
    subprocess.run(["python", "explore.py"])

def run_file3():
    subprocess.run(["python", "bard.py"])

# Create main window
root = tk.Tk()
root.title("Login/Signup")

# Login frame
login_frame = tk.Frame(root)
login_frame.pack(pady=10)

login_label = tk.Label(login_frame, text="Login")
login_label.grid(row=0, column=0, columnspan=2)

login_username_label = tk.Label(login_frame, text="Username")
login_username_label.grid(row=1, column=0)
login_username = tk.Entry(login_frame)
login_username.grid(row=1, column=1)

login_password_label = tk.Label(login_frame, text="Password")
login_password_label.grid(row=2, column=0)
login_password = tk.Entry(login_frame, show="*")
login_password.grid(row=2, column=1)

login_button = tk.Button(login_frame, text="Login", command=login)
login_button.grid(row=3, column=0, columnspan=2, pady=10)

# Signup frame
signup_frame = tk.Frame(root)
signup_frame.pack(pady=10)

signup_label = tk.Label(signup_frame, text="Signup")
signup_label.grid(row=0, column=0, columnspan=2)

signup_username_label = tk.Label(signup_frame, text="Username")
signup_username_label.grid(row=1, column=0)
signup_username = tk.Entry(signup_frame)
signup_username.grid(row=1, column=1)

signup_password_label = tk.Label(signup_frame, text="Password")
signup_password_label.grid(row=2, column=0)
signup_password = tk.Entry(signup_frame, show="*")
signup_password.grid(row=2, column=1)

signup_button = tk.Button(signup_frame, text="Signup", command=signup)
signup_button.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()