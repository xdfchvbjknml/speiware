import tkinter as tk # importing
import getpass
import os
root = tk.Tk()

img = tk.PhotoImage(file="spy.png")

label = tk.Label(root, image=img)
label.pack()

root.mainloop()
