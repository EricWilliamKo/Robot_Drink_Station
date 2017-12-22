from RobotStations.Arm import Arm
from RobotStations.Station import Station
from RobotStations.Drinks import Drink
from RobotStations.LockerManager import LockerManager
from threading import Timer
import serial

class ProcessController:

    def __init__(self):
        self.waitingList = list()
        self.processingList = list()
        self.drink_id = 0

        self.arm = Arm()
        self.arm.register(self.armNotification)
        
        self.stationSerial = serial.Serial("/dev/mega_station",9600)
        self.lockerManager = LockerManager(self.stationSerial)

        self.cupdropper = Station('cupdropper',self.stationSerial)
        self.iceStation = Station('ice',self.stationSerial)
        self.ingredientsStation = Station('ingredients',self.stationSerial)
        self.blackTeaStation = Station('black_tea',self.stationSerial)
        self.wmTeaStation = Station('wm_tea',self.stationSerial)
        self.sealerStation = Station('sealer',self.stationSerial)
        self.cupdropper.register(self.stationNotification)
        self.iceStation.register(self.stationNotification)
        self.ingredientsStation.register(self.stationNotification)
        self.blackTeaStation.register(self.stationNotification)
        self.wmTeaStation.register(self.stationNotification)
        self.sealerStation.register(self.stationNotification)
        self.stationDic = {'cupdropper':self.cupdropper,'ice':self.iceStation,'black_tea':self.blackTeaStation,
                    'wm_tea':self.wmTeaStation,'ingredients':self.ingredientsStation,'sealer':self.sealerStation}
        

    def getorder(self,neworders):
        print 'got order'
        for drink in neworders:
            drink.id = self.drink_id
            drink.manufacturingProcess.append('cupdropper')
            if drink.ingredients > 0:
                drink.manufacturingProcess.append('ingredients')
            if drink.ice > 0:
                drink.manufacturingProcess.append('ice')
            if drink.black_tea > 0:
                drink.manufacturingProcess.append('black_tea')
            if drink.wm_tea > 0:
                drink.manufacturingProcess.append('wm_tea')
            drink.manufacturingProcess.append('sealer')
            self.drink_id += 1 
            self.waitingList.append(drink)
        print 'waiting List', self.waitingList

        self.fromWaitingToProcess()
        return
            
    def getProcessingList(self):
        return self.processingList

    def getWaitingList(self):
        return self.waitingList

    def stationNotification(self,name,drink_id):
        drink = next((i for i in self.processingList if i.id == drink_id), None)
        station = self.stationDic[name]
        if station.stationName in ['ice','ingredients','black_tea','wm_tea']:
            drink.nextMove = 'move'
        elif station.stationName == 'sealer':
            drink.nextMove = 'lock'
        if self.waitingList != []:
            self.fromWaitingToProcess()
        self.scanArmMission()
        return

    def armNotification(self,msg,drink_id):
        print 'drink id ', str(drink_id)
        print 'drink details', self.processingList[0].__dict__
        drink = next((i for i in self.processingList if i.id == drink_id), None)
        drink.nextMove = msg
        
        if self.arm.status != 'waitfordropping':
            self.arm.cleanID()
        if msg == 'done':
            self.processingList.remove(drink)
            self.scanArmMission()
            if self.orderComplete(drink.order_id):
                self.lockerManager.orderComplete(drink.order_id)
                self.arm.goHome()

        self.dropCheck()
        self.scanStationMission()
        return

    def fromWaitingToProcess(self):
        if self.cupdropper.status == 'available':
            self.cupdropper.status = 'working'
            target = self.waitingList.pop(0)
            target.nextMove = 'drop'
            self.processingList.append(target)
            print 'processingList ',self.processingList
            self.dropCheck()
        return

    def dropCheck(self):
        if self.arm.isAvailable():
            for drink in self.processingList:
                if drink.nextMove == 'drop':
                    if self.stationDic[drink.manufacturingProcess[1]].status == 'available':
                        if self.arm.status == 'available':
                            print drink.manufacturingProcess[1],self.stationDic[drink.manufacturingProcess[1]].status
                            self.stationDic[drink.manufacturingProcess[1]].status = 'working'
                            self.arm.lockID(drink.id)
                            self.arm.getcup()

    def scanArmMission(self): 
        # print self.arm.status
        if self.arm.isAvailable():
            for drink in self.processingList:
                print 'scan Arm ',drink.__dict__
                if drink.nextMove == 'move':
                    nextStation = self.stationDic[drink.manufacturingProcess[1]]
                    thisStation = self.stationDic[drink.manufacturingProcess[0]]
                    if nextStation.status == 'available':
                        self.arm.lockID(drink.id)
                        self.arm.moveDrink(thisStation.getLocation(),nextStation.getLocation())
                        thisStation.status = 'available'
                        nextStation.status = 'working'
                        print nextStation.stationName, nextStation.status
                        drink.manufacturingProcess.remove(thisStation.stationName)
                        return
                elif drink.nextMove == 'lock':
                    if not self.lockerManager.isFull():
                        self.arm.lockID(drink.id)
                        locker = self.lockerManager.getEmptyLocker()
                        locker.storeDrink(drink)
                        self.sealerStation.status = 'available'
                        drink.manufacturingProcess.remove('sealer')
                        drink.nextMove = 'done'
                        self.arm.toLocker(locker.getLocation())
                        return
                else:
                    pass
        return

    def scanStationMission(self):
        for drink in self.processingList:
            try:
                nextStation = self.stationDic[drink.manufacturingProcess[1]]
            except:
                pass
            if drink.manufacturingProcess !=[]:
                thisStation = self.stationDic[drink.manufacturingProcess[0]]
                print drink.__dict__
                if drink.nextMove == 'drop':
                    print 'status = ',self.cupdropper.status
                    if self.cupdropper.status == 'working' and self.arm.status == 'waitfordropping':
                        self.cupdropper.work(1)
                        t = Timer(3,self.arm.moveDrink,[thisStation.getLocation(),nextStation.getLocation()])
                        t.daemon = True
                        t.start()
                        drink.manufacturingProcess.remove(thisStation.stationName)
                        self.cupdropper.status = 'available'
                if drink.nextMove == 'fill':
                    thisStation.processing_id = drink.id
                    thisStation.work(drink.getVolume(thisStation.stationName))
                elif drink.nextMove == 'seal':
                    thisStation.processing_id = drink.id
                    thisStation.work(1)
        return

    def orderComplete(self,order_id):
        complete = True
        for drink in self.waitingList:
            if drink.order_id == order_id:
                complete = False
        for drink in self.processingList:
            if drink.order_id == order_id:
                complete = False
        return complete


    
