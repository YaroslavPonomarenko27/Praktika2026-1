import tkinter as tk
from tkinter import filedialog

def open_file():
    path = filedialog.askopenfilename()
    label.config(text=path)

root = tk.Tk()
root.title("Файли")
root.geometry("500x300")

tk.Button(root, text="Відкрити файл", command=open_file).pack(pady=20)

label = tk.Label(root, text="", wraplength=450)
label.pack(pady=10)

root.mainloop()
