import serial
import time
import csv
from datetime import datetime
from threading import Timer
from collections import defaultdict
from heapq import *
from Queue import *

from Locker import Locker

class LockerManager:

    def __init__(self):
        self.locker1 = Locker(1)
        self.locker2 = Locker(2)
        self.locker3 = Locker(3)

    def connectMega(self):
        self.megaSerial = serial.Serial('/dev/mega',9600)

    def isFull(self):
        if self.locker1.isEmpty() or self.locker2.isEmpty() or self.locker3.isEmpty():
            return False
        else:
            return True

    def getEmptyLocker(self):
        if self.locker1.isEmpty():
            return self.locker1
        elif self.locker2.isEmpty():
            return self.locker2
        elif self.locker3.isEmpty():
            return self.locker3
