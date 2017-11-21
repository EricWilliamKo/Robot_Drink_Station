import serial
import time
import csv
from threading import Timer
from collections import defaultdict
from heapq import *
from Queue import *

class Arm:
    armSerial = serial.Serial('/dev/arm',115200)
    position = None
    status = None
    pathfile = open('path.csv','rb')
    cmdfile = open('path.csv','rb')
    workingQueue = Queue()

    def __init__(self):
        pathfile = csv.reader(self.pathfile,dialect = 'excel')
        cmdfile = csv.reader(self.cmdfile,dialect = 'excel')
        pathreader = csv.reader(pathfile,dialect = 'excel')
        cmdreader = csv.reader(cmdfile,dialect = 'excel')

        #make csv dictionary
        self.pathDic = defaultdict(list)
        self.cmdDic = defaultdict(list)
        for l,r,c in pathreader:
            self.pathDic[l].append((int(c),r))
        for pose,cmd in cmdreader:
            self.cmdDic[pose].append(cmd)

        #initialize arm pose
        self.armSerial.write(self.cmdDic['P0'])
        self.position = 'P0'

    def register(self,sub):
        self.subsciber = sub
    
    def notifyController(self,msg):
        self.subsciber(msg)

    def moveDrink(self,start,destination):
        if start != self.position:
            self.moveToTarget(start)

    def moveToTarget(self,targetPosition):
        path = self.calculatePath(self.position,targetPosition)
        for stop in path:
            self.workingQueue.put((self.moveToNext,stop))

    def moveTarget(self,destination):
        path = self.calculatePath(self.position,destination)
        self.workingQueue.put(self.grab,())
        for stop in path:
            self.workingQueue.put(self.moveToTarget,stop)
        self.workingQueue.put(self.release,())
            


    def calculatePath(self,start,destination):
        try:
            (cost,path) = self.dijkstra(self.pathDic,start,destination)
            print 'cost = ',cost
            print 'path = ',path
        except:
            print 'path error'
            return None
        
        return path

    def dijkstra(self,pathdic, f, t):
        pathBuf = list()
        q, seen = [(0,f,pathBuf)], set()
        while q:
            (cost,v1,path) = heappop(q)
            if v1 not in seen:
                seen.add(v1)
                path.append(v1)
                if v1 == t: return (cost, path)

                for c, v2 in pathdic.get(v1, ()):
                    if v2 not in seen:
                        dicpath = path[0:]
                        heappush(q, (cost+c, v2, dicpath))
                        dicpath = []

        return float("inf")

    def grab(self):
        return

    def release(self):
        return

    def moveToNext(self,destination):
        self.armSerial.write(self.cmdDic[destination])
        self.position = destination
        if not self.workingQueue.empty():
            Timer.
        
        

