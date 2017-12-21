import serial
import time
import csv
from datetime import datetime
from threading import Timer
from collections import defaultdict
from heapq import *
from Queue import *

class Arm:
    
    

    def __init__(self):
        self.armSerial = serial.Serial('/dev/arm',115200)
        pathfile = open('arm_path.csv','rb')
        cmdfile = open('position.csv','rb')
        pathreader = csv.reader(pathfile,dialect = 'excel')
        cmdreader = csv.reader(cmdfile,dialect = 'excel')
        self.workingList = list()
        self.processing_id = None

        #make csv dictionary
        self.pathDic = defaultdict(list)
        self.cmdDic = {}
        for l,r,c,mtime in pathreader:
            self.pathDic[l].append((int(c),r,mtime))
        for pose,cmd in cmdreader:
            self.cmdDic[pose] = cmd

        # initialize arm pose
        # self.armSerial.write(self.cmdDic['P0'])
        self.sendArmCmd('P0','1000')
        self.position = 'P0'
        self.status = 'available'

        print 'status = ',self.status
        print 'position = ', self.position
        print self.pathDic
        print self.cmdDic
        print 'initialize complete!!'

    def register(self,notifyFunc):
        self.notifyFunc = notifyFunc
    
    def notify(self,msg):
        self.notifyFunc(msg,self.processing_id)

    def lockID(self,drink_id):
        self.processing_id = drink_id

    def cleanID(self):
        self.processing_id = None

    def isAvailable(self):
        if self.status == 'available':
            return True
        else:
            return False

    def getcup(self):
        print 'get cup'
        self.status = 'working'
        if self.position != 'S1':
            self.moveToTarget('S1')
            self.workingList.append((self.grab,'grab'))
        (func,arg) = self.workingList.pop(0)
        func(arg)

    def toLocker(self,lockerLocation):
        print 'to locker ',lockerLocation
        self.status = 'working'
        self.moveDrink('S6I',lockerLocation)

    def moveDrink(self,start,destination):
        self.status = 'working'
        if start != self.position:
            self.moveToTarget(start)
            self.moveTarget(start,destination)
        else:
            self.moveTarget(start,destination)
        # print self.workingList
        (func,arg) = self.workingList.pop(0)
        func(arg)

    def moveToTarget(self,targetPosition):
        path = self.calculatePath(self.position,targetPosition)
        for stop in path:
            self.workingList.append((self.moveToNext,stop))

    def moveTarget(self,start,destination):
        path = self.calculatePath(start,destination)
        self.workingList.append((self.grab,'grab'))
        # print path
        for stop in path:
            self.workingList.append((self.moveToNext,stop))
        self.workingList.append((self.release,'release'))
            


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

                for c, v2, wtime in pathdic.get(v1, ()):
                    if v2 not in seen:
                        path2 = path[0:]
                        heappush(q, (cost+c, v2, path2))
                        path2 = []

        return float("inf")

    def sendArmCmd(self,destination,workingTime):
        end = '\r\n'
        pose = self.cmdDic[destination]
        command = pose + 'T' + workingTime + end
        self.armSerial.write(command)
        print command

    def grab(self,cmd):
        print cmd
        print datetime.now().time()        
        if self.workingList != []:
            (func,arg) = self.workingList.pop(0)
            # print 'from grab',func,arg
            t = Timer(1,func,[arg])
            t.daemon = True
            t.start()
        else:
            self.status = 'waitfordropping'
            print 'job done!!'
            self.notify('drop')
            return
        

    def release(self,cmd):
        print cmd
        print datetime.now().time()        
        if self.workingList != []:
            (func,arg) = self.workingList.pop(0)
            # print 'from release',func,arg
            t = Timer(1,func,[arg])
            t.daemon = True
            t.start()
        else:
            self.status = 'available'
            print 'job done!!'
            if self.position == 'S6':
                self.notify('seal')
            elif self.position in ['L1','L2','L3']:
                self.notify('done')
            else:
                self.notify('fill')
            return
        

    def moveToNext(self,destination):
        # print 'positoin = ',self.position
        # print 'destination = ',destination
        if self.workingList != []:
            (func,arg) = self.workingList.pop(0)
        else:
            self.status = 'available'
            print 'job done!!'
            return
        if self.position == destination:
            print 'pass first station'
            func(arg)
            return
        for c, v2, wtime in self.pathDic.get(self.position, ()):
            if v2 == destination:
                workingTime = float(wtime)/1000
                print datetime.now().time()
                self.sendArmCmd(destination,wtime)
                # self.armSerial.write(self.cmdDic[destination])
                self.position = destination
                t = Timer(workingTime,func,[arg])
                t.daemon = True
                t.start()
                print self.processing_id, ' moving to ',destination
                return
        

