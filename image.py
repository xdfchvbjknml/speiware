import tkinter as tk
root = tk.Tk()

img = tk.PhotoImage(file="spy.png")

label = tk.Label(root, image=img)
label.pack()

root.mainloop()