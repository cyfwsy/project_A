import time
from threading import Thread

def countdown(n):
    while n > 0:
        print('counting')
        print()
        n -= 1
        time.sleep(1)
c = Thread(target=countdown,args=(5,))
c.start()
print('starting thread ')
c.join()
print('ending thread')
