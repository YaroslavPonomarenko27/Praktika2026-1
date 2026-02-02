import tkinter as tk

root = tk.Tk()
root.title("Компоненти")
root.geometry("400x300")

tk.Label(root, text="Ім'я").grid(row=0, column=0, padx=10, pady=10)
tk.Entry(root).grid(row=0, column=1)

tk.Label(root, text="Пароль").grid(row=1, column=0, padx=10)
tk.Entry(root, show="*").grid(row=1, column=1)

tk.Button(root, text="Увійти").grid(row=2, column=0, columnspan=2, pady=20)

root.mainloop()
