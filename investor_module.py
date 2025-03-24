import tkinter as tk
import csv
from tkinter import messagebox

# Function to display products
def view_products():
    with open('products.csv', 'r') as file:
        reader = csv.reader(file)
        products = "\n".join([f"{row[0]} - ₹{row[1]}" for row in reader])
    messagebox.showinfo("Products", products)

# Function to view entrepreneurs
def view_entrepreneurs():
    with open('entrepreneurs.csv', 'r') as file:
        reader = csv.reader(file)
        entrepreneurs = "\n".join([f"{row[0]} ({row[1]})" for row in reader])
    messagebox.showinfo("Entrepreneurs", entrepreneurs)

# GUI for investor functionalities
root = tk.Tk()
root.title("HerMark - Investor")
root.geometry("500x400")
root.configure(bg='#f0f0f0')

tk.Label(root, text="Investor Dashboard", font=("Helvetica", 16), bg='#f0f0f0').pack(pady=20)

btn_products = tk.Button(root, text="View Products", command=view_products, bg='#4caf50', fg='white')
btn_products.pack(pady=10)

btn_entrepreneurs = tk.Button(root, text="View Entrepreneurs", command=view_entrepreneurs, bg='#2196f3', fg='white')
btn_entrepreneurs.pack(pady=10)

root.mainloop()