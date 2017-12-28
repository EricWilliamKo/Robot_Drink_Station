import threading
import time
from threading import Timer

lst = ['name1', 'name2', 'name3','name4', "a"]

def doWork(param):
    for i, name in enumerate(param):
        time.sleep(0.5)
        print i, name

workThread = threading.Thread(target=doWork, args=(lst,))
workThread.start()