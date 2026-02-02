import tkinter as tk
from tkinter import messagebox

def show_info():
    messagebox.showinfo("Інфо", "Це діалогове вікно")

root = tk.Tk()
root.title("Меню")
root.geometry("400x300")

menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu, tearoff=0)
file_menu.add_command(label="Інформація", command=show_info)
file_menu.add_command(label="Вихід", command=root.destroy)

menu.add_cascade(label="Файл", menu=file_menu)

root.mainloop()
