import tkinter as tk
from tkinter import ttk
import mysql.connector
from mysql.connector import Error

# Function to connect to MySQL and fetch data from the selected table
def fetch_data(table_name):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='legal_link',
                                             user='root',
                                             password='123456789')
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute(f"SELECT * FROM {table_name}")
            records = cursor.fetchall()
            connection.close()
            return records
    except Error as e:
        print("Error while connecting to MySQL", e)

# Function to handle the selection event of the combobox
def on_select(event):
    selected_table = table_combobox.get()
    if selected_table:
        records = fetch_data(selected_table)
        if records:
            # Clearing previous data from the treeview
            for row in treeview.get_children():
                treeview.delete(row)
            # Inserting new data into the treeview
            for record in records:
                treeview.insert('', 'end', values=record)

# Creating the main window
root = tk.Tk()
root.title("MySQL Table Viewer")

# Creating a frame for the combobox and treeview
frame = ttk.Frame(root)
frame.pack(padx=10, pady=10)

# Creating the combobox to select the table
table_label = ttk.Label(frame, text="Select Table:")
table_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

table_combobox = ttk.Combobox(frame, state="readonly")
table_combobox.grid(row=0, column=1, padx=5, pady=5, sticky="w")

# Populating the combobox with table names
table_names = ['civil_lawyer', 'corporate_lawyer', 'criminal_lawyer','domestic_lawyer','education_lawyer','environmental_lawyer','estate_lawyer','healthcare_lawyer' , 'human_rights_lawyer' , 'immigration_lawyer' , 'patent_lawyer' , 'tax_lawyer']  # Replace with actual table names
table_combobox['values'] = table_names

# Binding the selection event of the combobox to the on_select function
table_combobox.bind("<<ComboboxSelected>>", on_select)

# Creating the treeview to display table data
treeview = ttk.Treeview(frame, columns=('specialization', 'name', 'contact_num', 'lawyer_id', 'base_fee'), show="headings")
for col in ('specialization', 'name', 'contact_num', 'lawyer_id', 'base_fee'):
    treeview.heading(col, text=col)
treeview.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
