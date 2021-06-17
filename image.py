import tkinter as tk
import getpass
import os
#importowanie gowna
root = tk.Tk()

img = tk.PhotoImage(file="spy.png")

label = tk.Label(root, image=img)
label.pack()

root.mainloop()
#tworzenie okienka ze szpiegiem