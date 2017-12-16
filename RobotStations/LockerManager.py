import serial
import time
import csv
import threading
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
        self.lockerList = [self.locker1,self.locker2,self.locker3]
        self.completedOrder = []
        self.processingOrder = []
        # self.connectMega()
        print 'locker ready'

    def read_from_port(self,ser):
        while self.megaConnected:
            time.sleep(0.005)
            if ser.inWaiting() > 5 :
                head = ser.read()
                if head == 'S':
                    num = ser.read(4)
                    end = ser.read()
                    if end == 'E':
                        self.unlockDrink(int(num))
                        print 'number = ',num

    def connectMega(self):
        self.megaConnected = True
        megaSerial = serial.Serial('/dev/mega',9600)
        serilThread = threading.Thread(target=self.read_from_port,args=(megaSerial,))
        serilThread.start()

    def disConnectMega(self):
        self.megaConnected = False

    def isFull(self):
        for locker in self.lockerList:
            if locker.isEmpty():
                return False

        return True

    def getEmptyLocker(self):
        for locker in self.lockerList:
            if locker.isEmpty():
                return locker

    def orderComplete(self,order_id):
        print 'Complete order id %d'%order_id
        self.processingOrder.remove(order_id)
        self.completedOrder.append(order_id)

    def addProcessingOrder(self,order_id):
        self.processingOrder.append(order_id)

    def unlockDrink(self,inputNum):
        inputError = True

        for order_id in self.processingOrder:
            if order_id == inputNum:
                inputError = False
                print 'Youe order is still processing, please wait a moment'
                return

        for order_id in self.completedOrder:
            if order_id == inputNum:
                for locker in self.lockerList:
                    if locker.drink.order_id == order_id:
                        locker.unlockDrink()
                        inputError = False
        
        if inputError:
            print 'input error'
            return
        else:
            print 'Please take your drinks'
            self.completedOrder.remove(inputNum)
            return