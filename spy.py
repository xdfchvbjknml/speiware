import os
from random import random
import time
import tkinter as tk
#importowanie
from threading import Thread

def func1():
    os.system("python C:/spei/window1.py")
    

def func2():
    os.system("python C:/spei/rtd.py")
    time.sleep(10)
if __name__ == '__main__':
    Thread(target = func1).start()
    Thread(target = func2).start()
window = tk.Tk()
window.title( "Spyvirus2.0" )
text = tk.StringVar()
label = tk.Label( window, textvariable = text, padx=100, pady=20)
label.pack()
text.set("SPY IS HACKING UR PC")
description = tk.Label(window, text="any last words?:").pack()
name = tk.Entry(window,width=40)
name.pack()
def Spyvirusmain():
    text.set("{0}- I WILL NOT READ THIS, HERE GO FUCK YOURSELF ".format(name.get()))
ok = tk.Button(window, text="OK", width=20, command=Spyvirusmain)
ok.pack()
os.system("C:\spei\image.py")
#okno ktore jest nie potrzebne ale flex bo jestem debilem
#jakos dziala
#tak komenatrze som pod dolem tego co komentujom bo jestem zjebem
for i in range(128):
    os.system("C:\spei\weird.py")
#po co ja to zrobilem nie pamietam po co xd
#rewite bede musial zrobiec ehhh
