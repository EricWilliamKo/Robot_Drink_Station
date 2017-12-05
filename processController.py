from RobotStations.Arm import Arm
from RobotStations.Station import Station
from RobotStations.Drinks import Drink
from RobotStations.LockerManager import LockerManager
from threading import Timer

class ProcessController:

    def __init__(self):
        self.waitingList = list()
        self.processingList = list()
        self.drink_id = 0

        self.arm = Arm()
        self.arm.register(self.armNotification)

        self.lockerManager = LockerManager()

        self.cupdropper = Station('cupdropper')
        self.iceStation = Station('ice')
        self.ingredientsStation = Station('ingredients')
        self.blackTeaStation = Station('black_tea')
        self.wmTeaStation = Station('wm_tea')
        self.sealerStation = Station('sealer')
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

        self.dropCheck()
        self.scanStationMission()
        return

    def fromWaitingToProcess(self):
        if self.cupdropper.status == 'available':
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
                        drink.manufacturingProcess.remove(thisStation.stationName)
                        return
                elif drink.nextMove == 'lock':
                    if not self.lockerManager.isFull():
                        self.arm.lockID(drink.id)
                        locker = self.lockerManager.getEmptyLocker()
                        locker.storeDrink(drink.id)
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
                    if self.cupdropper.status == 'available' and self.arm.status == 'waitfordropping':
                        self.cupdropper.work(1)
                        Timer(3,self.arm.moveDrink,[thisStation.getLocation(),nextStation.getLocation()]).start()
                        drink.manufacturingProcess.remove(thisStation.stationName)
                        # drink.status = 'fill'
                if drink.nextMove == 'fill':
                    thisStation.processing_id = drink.id
                    thisStation.work(drink.getVolume(thisStation.stationName))
                elif drink.nextMove == 'seal':
                    thisStation.processing_id = drink.id
                    thisStation.work(1)
        return


    
