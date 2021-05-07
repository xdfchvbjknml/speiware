import os
from random import random
import time
import tkinter as tk
#importowanie

window = tk.Tk()
window.title( "ERROR" )
label = tk.Label( window, text = "very bad connection to our server wait 30 seconds" )
label.pack( side = tk.BOTTOM )
tk.mainloop()
time.sleep(5)
os.system("python C:\spei\image.py")
os.system("python C:\spei\rtd.py")
#playing suprise buttsecks
window = tk.Tk()
window.title( "Spyvirus 2.0" )
text = tk.StringVar()
label = tk.Label( window, textvariable = text, padx=100, pady=20)
label.pack()
text.set("SPY IS HACKING UR PC")
description = tk.Label(window, text="DO YOU HAVE SPECIAL MESSAGE TO SPY???:").pack()
name = tk.Entry(window,width=40)
name.pack()
def Spyvirusmain():
    text.set("{0}- I WILL NOT READ THIS, HERE GO FUCK YOURSELF ".format(name.get()))
ok = tk.Button(window, text="OK", width=20, command=Spyvirusmain)
ok.pack()
for i in range(128):
    os.systen("C:\spei\weird.py")
#po co ja to zrobilem nie pamietam po co xd
#rewite bede musial zrobiec ehhh