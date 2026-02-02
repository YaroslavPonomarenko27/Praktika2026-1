import tkinter as tk

root = tk.Tk()
root.title("Графічний застосунок")
root.geometry("400x300")

label = tk.Label(root, text="Мій перший GUI", font=("Arial", 16))
label.pack(pady=40)

root.mainloop()
