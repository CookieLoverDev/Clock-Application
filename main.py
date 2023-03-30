import tkinter as tk
from datetime import datetime as dt

def upade_time():
    now = dt.now()
    time = now.strftime("%H:%M:%S")
    label.config(text = time)
    label.after(1000, upade_time)

root = tk.Tk()
root.title("Tick Tock")
root.resizable(0, 0)

label = tk.Label(root, font=("ds-digital", 80), bg="black", fg="cyan")
label.pack(anchor="center")

upade_time()
root.mainloop()