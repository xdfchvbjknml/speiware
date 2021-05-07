from threading import Thread

def one():
    while(1 == num):
        os.system(image.py)
    
def two():
    while(1 == num):
        os.system(downloader.cmd)


p1 = Thread(target = one)
p2 = Thread(target = two)

p1.start()
p2.start()