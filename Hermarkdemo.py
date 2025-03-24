import tkinter as tk
from tkinter import messagebox, filedialog, ttk
from PIL import Image, ImageTk
import csv
import subprocess
import os
# --- User Registration & Login ---
def register():
    username = entry_username.get()
    password = entry_password.get()

    if username and password:
        with open("users.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([username, password])
        messagebox.showinfo("Success", "Registered Successfully!")
    else:
        messagebox.showerror("Error", "Please enter username and password!")

def login():
    username = entry_username.get()
    password = entry_password.get()
    
    if not os.path.exists("users.csv"):
        messagebox.showerror("error")
        return
    with open("users.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row == [username, password]:
                messagebox.showinfo("Success", "Login Successful!")
                login_window.destroy()
                subprocess.Popen(["python","main.py"])
                
                break
            else:
                messagebox.showerror("Error", "Invalid Credentials")
          
                             


# --- Main Window (Login) ---
login_window = tk.Tk()
login_window.title("HerMark - Login")
login_window.geometry("500x600")

tk.Label(login_window, text="Username").grid(row=0)
tk.Label(login_window, text="Password").grid(row=1)

entry_username = tk.Entry(login_window)
entry_password = tk.Entry(login_window, show="*")
entry_username.grid(row=0, column=1)
entry_password.grid(row=1, column=1)

tk.Button(login_window, text="Register", command=register).grid(row=2, column=0)
tk.Button(login_window, text="Login", command=login).grid(row=2, column=1)

    
login_window.mainloop()
