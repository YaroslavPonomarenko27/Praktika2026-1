# utils.py
def greet():
    return (["Модуль"])

# main.py
import tkinter as tk
from utils import greet()

root = tk.Tk()
root.title("Модулі")
root.geometry("400x300")

tk.Label(root, text=greet(), font=("Arial", 14)).pack(pady=50)

root.mainloop()
