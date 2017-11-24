import time
from threading import Timer

class Station:


    def __init__(self,stationName):
        self.status = "empty"
        self.remain = 100
        self.drink = None
        self.stationName = stationName
        self.processing_id = None
    
    def register(self,notifyFunc):
        self.notifyFunc = notifyFunc

    def notify(self, msg):
        self.notifyFunc(msg)
