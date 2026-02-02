import tkinter as tk

def on_click():
    label.config(text="Кнопку натиснуто")

root = tk.Tk()
root.title("Події")
root.geometry("400x300")

label = tk.Label(root, text="Очікую подію", font=("Arial", 14))
label.pack(pady=20)

button = tk.Button(root, text="Натисни", command=on_click)
button.pack(pady=20)

root.mainloop()
