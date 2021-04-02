import tkinter as tk # importing
import getpass
import os

os.system("python image.py")
window = tk.Tk() # making window
window.title( "Spyvirus1.0" ) # title
text = tk.StringVar()
label = tk.Label( window, textvariable = text, padx=100, pady=20)
label.pack()
text.set("Dear SPY IS HACKING UR PC")
description = tk.Label(window, text="DO YOU HAVE SPECIAL MESSAGE TO SPY???:").pack()
name = tk.Entry(window,width=40)
name.pack()
def Spyvirusmain():
    text.set("{0}- I WILL NOT READ THIS, HERE GO FUCK YOURSELF ".format(name.get()))
ok = tk.Button(window, text="OK", width=20, command=Spyvirusmain)
ok.pack()
os.system("bashwannabe.cmd")

tk.mainloop() # loop
