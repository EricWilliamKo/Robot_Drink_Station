import serial
import time
import csv
from motion_module import MotionModule
from datetime import datetime
from threading import Timer
from collections import defaultdict
from heapq import *
from Queue import *

class Arm:
    
    

    def __init__(self):
        pathfile = open('arm_path.csv','rb')
        cmdfile = open('position.csv','rb')
        pathreader = csv.reader(pathfile,dialect = 'excel')
        self.mm = MotionModule()
        self.workingList = list()
        self.processing_id = None

        #make csv dictionary
        self.pathDic = defaultdict(list)
        for l,r,c,mtime in pathreader:
            self.pathDic[l].append((int(c),r,mtime))
        

        # initialize arm pose
        self.mm.toP0('1000')
        self.position = 'P0'
        self.status = 'available'

        print 'status = ',self.status
        print 'position = ', self.position
        print self.pathDic
        print 'initialize complete!!'

    def register(self,notifyFunc):
        self.notifyFunc = notifyFunc
        
    
    def notify(self,msg):
        print datetime.now().time()
        print 'arm job done!!'
       
        if msg == 'drop' :
            self.status = 'waitfordropping'
        else:
            self.status = 'available'
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
        if self.position != 'P1':
            self.moveToTarget('P1')
            self.workingList.append((self.release,'S1'))
            self.workingList.append((self.notify,'drop'))
        
        print self.workingList
        (func,arg) = self.workingList.pop(0)
        func(arg)

    def pullcup(self,nextStation):
        print 'pull cup'
        self.status = 'working'
        # print 'position = ' + self.position
        # print 'next = ' nextStation
        self.moveDrink('S1',nextStation)

    def toLocker(self,lockerLocation):
        print 'to locker ',lockerLocation
        self.status = 'working'
        self.moveDrink('S6I',lockerLocation)

    def moveDrink(self,start,destination):
        self.status = 'working'
        if self.psoeReady(start, self.position):
            print 'pose ready'
            self.moveTarget(start ,destination)
        else:
            print 'pose not ready'
            self.moveToTarget(self.getPrepose(start))
            self.moveTarget(start,destination)
        print self.workingList
        (func,arg) = self.workingList.pop(0)
        func(arg)

    def moveToTarget(self,targetPosition):
        path = self.calculatePath(self.position,targetPosition)
        for stop in path:
            self.workingList.append((self.moveToNext,stop))

    def moveTarget(self,start,destination):
        path = self.calculatePath(self.getPrepose(start), self.getPrepose(destination))
        self.workingList.append((self.grab,start))
        for stop in path:
            self.workingList.append((self.moveToNext,stop))
        self.workingList.append((self.release,destination))
        notifyMsg = {'S2':'fill','S3':'fill','S4':'fill','S5':'fill','S6':'seal',
                    'L1':'done','L2':'done','L3':'done'}
        self.workingList.append((self.notify,notifyMsg[destination]))

    def goHome(self):
        print 'Go Home'
        self.moveToTarget('P0')
        self.workingList.append((self.notify,'done'))
        (func,arg) = self.workingList.pop(0)
        func(arg)

    def psoeReady(self,target,pose):
        preposeDic = {'S1':'P1','S2':'P2','S3':'P3','S4':'P4','S5':'P5','S6':'P6','S6I':'P6I'}
        if pose == preposeDic[target]:
            return True
        else:
            return False

    def getPrepose(self,tartget):
        preposeDic = {'S1':'P1','S2':'P2','S3':'P3','S4':'P4','S5':'P5','S6':'P6','S6I':'P6I',
                        'L1':'P6I','L2':'P6I','L3':'P6I'}
        return preposeDic[tartget]


    def calculatePath(self,start,destination):
        # print 'cal path ' + start + 'to' + destination
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


    def grab(self,station):
        print self.processing_id,' get '+ station
        motionDic = {'S1':self.mm.pullCup,'S2':self.mm.getS2,'S3':self.mm.getS3,'S4':self.mm.getS4,
                    'S5':self.mm.getS5,'S6I':self.mm.getS6I}

        print datetime.now().time()
        wtime = motionDic[station]()        
        if self.workingList != []:
            (func,arg) = self.workingList.pop(0)
            t = Timer(wtime,func,[arg])
            t.daemon = True
            t.start()
        else:
            print 'job done!!'
            return
        

    def release(self,station):
        print self.processing_id,' put '+ station
        motionDic = {'S1':self.mm.getCup, 'S2':self.mm.putS2,'S3':self.mm.putS3,'S4':self.mm.putS4,
                    'S5':self.mm.putS5,'S6':self.mm.putS6,
                    'L1':self.mm.putL1,'L2':self.mm.putL2,'L3':self.mm.putL3}

        print datetime.now().time()
        wtime = motionDic[station]()        
        if self.workingList != []:
            (func,arg) = self.workingList.pop(0)
            t = Timer(wtime,func,[arg])
            t.daemon = True
            t.start()
        else:
            print 'job done'
            return
        

    def moveToNext(self,destination):
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
                self.mm.toGoal(destination,wtime)
                self.position = destination
                t = Timer(workingTime,func,[arg])
                t.daemon = True
                t.start()
                print self.processing_id, ' moving to ',destination
                return


        

