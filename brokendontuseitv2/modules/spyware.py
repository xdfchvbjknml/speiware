import tkinter as tk
import getpass
import os
from random import random
import threading
import time
import winsound



import tkinter as tk




print("Sorry, you will need to wait")
time.sleep(3)
print("Our servers are too overloaded!")
os.system("python dasdas.py https://www.youtube.com/watch?v=Pry9d8pWfd0")
os.system("choco install ffmpeg")
time.sleep(30)
window = tk.Tk()
window.title( "ERROR" )
label = tk.Label( window, text = "very bad connection to our server wait 30 seconds" )
label.pack( side = tk.BOTTOM )
tk.mainloop()
winsound.PlaySound("bettersounds.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
time.sleep(5)
os.system("python image.py")
os.system("python rtd.py")
window = tk.Tk()
window.title( "Spyvirus1.0" )
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
for i in range(128):
    os.systen("weird.py")
