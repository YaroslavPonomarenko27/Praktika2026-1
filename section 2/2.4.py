import tkinter as tk

def calculate():
    result = int(entry1.get()) + int(entry2.get())
    label.config(text=f"Результат: {result}")

root = tk.Tk()
root.title("Обчислення")
root.geometry("400x300")

entry1 = tk.Entry(root)
entry1.pack(pady=5)

entry2 = tk.Entry(root)
entry2.pack(pady=5)

tk.Button(root, text="Обчислити", command=calculate).pack(pady=10)

label = tk.Label(root, text="")
label.pack(pady=10)

root.mainloop()
