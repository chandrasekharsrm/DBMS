import tkinter as tk
import mysql.connector

def insert_data():
    user_name = user_name_entry.get()
    client_id = client_id_entry.get()
    name = name_entry.get()
    ph_number = ph_number_entry.get()
    address = address_entry.get()
    lawyer_id = lawyer_id_entry.get()
    case_type = case_type_entry.get()

    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="123456789",
            database="legal_link"
        )

        cursor = connection.cursor()

        sql_query = "INSERT INTO client (user_name, client_id, name, ph_number, address, lawyer_id, type) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        data = (user_name, client_id, name, ph_number, address, lawyer_id, case_type)

        cursor.execute(sql_query, data)
        connection.commit()

        cursor.close()
        connection.close()

        status_label.config(text="Data inserted successfully!", fg="green")
    except Exception as e:
        status_label.config(text=f"Error: {str(e)}", fg="red")

# GUI setup
root = tk.Tk()
root.title("MySQL Data Entry")

user_name_label = tk.Label(root, text="User Name:")
user_name_label.grid(row=0, column=0, padx=10, pady=5)
user_name_entry = tk.Entry(root)
user_name_entry.grid(row=0, column=1, padx=10, pady=5)

client_id_label = tk.Label(root, text="Client ID:")
client_id_label.grid(row=1, column=0, padx=10, pady=5)
client_id_entry = tk.Entry(root)
client_id_entry.grid(row=1, column=1, padx=10, pady=5)

name_label = tk.Label(root, text="Name:")
name_label.grid(row=2, column=0, padx=10, pady=5)
name_entry = tk.Entry(root)
name_entry.grid(row=2, column=1, padx=10, pady=5)

ph_number_label = tk.Label(root, text="Phone Number:")
ph_number_label.grid(row=3, column=0, padx=10, pady=5)
ph_number_entry = tk.Entry(root)
ph_number_entry.grid(row=3, column=1, padx=10, pady=5)

address_label = tk.Label(root, text="Address:")
address_label.grid(row=4, column=0, padx=10, pady=5)
address_entry = tk.Entry(root)
address_entry.grid(row=4, column=1, padx=10, pady=5)

lawyer_id_label = tk.Label(root, text="Lawyer ID:")
lawyer_id_label.grid(row=5, column=0, padx=10, pady=5)
lawyer_id_entry = tk.Entry(root)
lawyer_id_entry.grid(row=5, column=1, padx=10, pady=5)

case_type_label = tk.Label(root, text="Case Type:")
case_type_label.grid(row=6, column=0, padx=10, pady=5)
case_type_entry = tk.Entry(root)
case_type_entry.grid(row=6, column=1, padx=10, pady=5)

insert_button = tk.Button(root, text="Insert Data", command=insert_data)
insert_button.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

status_label = tk.Label(root, text="", fg="green")
status_label.grid(row=8, column=0, columnspan=2)

root.mainloop()
