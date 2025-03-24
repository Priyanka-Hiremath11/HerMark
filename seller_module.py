import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
import csv

# Function to upload product data
def upload_product():
    name = entry_name.get()
    price = entry_price.get()
    image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.png")])

    if name and price and image_path:
        with open('products.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, price, image_path])
        messagebox.showinfo("Success", "Product uploaded successfully!")
    else:
        messagebox.showerror("Error", "Please fill all fields")

# Function to simulate mock interview
def mock_interview():
    questions = [
        "Tell us about your business?",
        "What makes your product unique?",
        "How will you scale your business?",
    ]
    answers = []
    for q in questions:
        ans = simpledialog.askstring("Interview", q)
        answers.append(ans)

    with open('interviews.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(answers)

    messagebox.showinfo("Success", "Mock interview saved!")

# GUI for seller functionalities
root = tk.Tk()
root.title("HerMark - Seller")
root.geometry("500x400")
root.configure(bg='#f0f0f0')

# Labels and entries
tk.Label(root, text="Product Name:", bg='#f0f0f0').pack(pady=5)
entry_name = tk.Entry(root, width=40)
entry_name.pack(pady=5)

tk.Label(root, text="Product Price:", bg='#f0f0f0').pack(pady=5)
entry_price = tk.Entry(root, width=40)
entry_price.pack(pady=5)

btn_upload = tk.Button(root, text="Upload Product", command=upload_product, bg='#4caf50', fg='white')
btn_upload.pack(pady=10)

btn_interview = tk.Button(root, text="Mock Interview", command=mock_interview, bg='#2196f3', fg='white')
btn_interview.pack(pady=10)

root.mainloop()