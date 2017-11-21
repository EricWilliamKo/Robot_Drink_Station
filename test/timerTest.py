import time
from threading import Timer
import threading

def print_time():
    print "From print_time", time.time()

def print_some_times():
    print time.time()
    Timer(5, print_time, ()).start()
    Timer(10, print_time, ()).start()
    time.sleep(11)  # sleep while time-delay events execute
    print time.time()

def moveToNext(path):
    nextItem = path.pop(0)
    print nextItem
    if path == []:
        print 'empty'
        return
    else:
        t = threading.Timer(0.5,moveToNext,[path])
        t.start()

    

        


path = ['a','b','c','d']
moveToNext(path)
# print_some_times()

