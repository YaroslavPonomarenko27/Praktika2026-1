import tkinter as tk

root = tk.Tk()
root.title("Canvas")
root.geometry("500x400")

canvas = tk.Canvas(root, bg="white")
canvas.pack(fill="both", expand=True)

canvas.create_rectangle(50, 50, 200, 150, fill="blue")
canvas.create_oval(250, 50, 400, 150, fill="red")

root.mainloop()
