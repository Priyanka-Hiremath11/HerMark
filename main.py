import tkinter as tk
from tkinter import messagebox
import tkinter as tk
from tkinter import messagebox, filedialog, ttk
from PIL import Image, ImageTk
import csv


# Function to handle user selection
def open_seller():
    messagebox.showinfo("Selection", "You selected Seller")
    root.destroy()
    import seller_module # Opens seller functionalities

def open_investor():
    messagebox.showinfo("Selection", "You selected Investor")
    root.destroy()
    import investor_module # Opens investor functionalities

# Create main window
root = tk.Tk()
root.title("HerMark - Select User Type")
root.geometry("400x300")
root.configure(bg='#f0f0f0')

# Labels and buttons
label = tk.Label(root, text="Are you an Investor or a Seller?", font=("Helvetica", 14), bg='#f0f0f0')
label.pack(pady=20)

btn_seller = tk.Button(root, text="Seller", command=open_seller, width=15, font=("Helvetica", 12), bg='#4caf50', fg='white')
btn_seller.pack(pady=10)

btn_investor = tk.Button(root, text="Investor", command=open_investor, width=15, font=("Helvetica", 12), bg='#2196f3', fg='white')
btn_investor.pack(pady=10)

root.mainloop()