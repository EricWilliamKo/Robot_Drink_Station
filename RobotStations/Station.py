import time
from threading import Timer

class Station:
    status = "empty"
    remain = 100
    drink = None

    def __init__(self):
        self.subscribers = set()
    
    def register(self,notifyFunc):
        self.notifyFunc = notifyFunc
    
    def unregister(self, subscreber):
        self.subscribers.discard(subscreber)

    def notify(self, msg):
        for subscriber in self.subscribers:
            subscriber.update(msg)

