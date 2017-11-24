from RobotStations.Arm import Arm
from RobotStations.Station import Station
from RobotStations.Drinks import Drink

class ProcessController:

    def __init__(self):
        self.waitingList = list()
        self.processingList = list()
        self.drink_id = 0

        self.arm = Arm()
        self.arm.register(self.armNotification)

        self.cupdropper = Station('cupdropper')
        self.iceStation = Station('ice')
        self.ingredientsStation = Station('ingredients')
        self.sealerStation = Station('sealer')
        self.cupdropper.register(self.stationNotification)
        self.iceStation.register(self.stationNotification)
        self.ingredientsStation.register(self.stationNotification)
        self.sealerStation.register(self.stationNotification)

    def getorder(self,neworders):
        for drink in neworders:
            drink.id = self.drink_id
            drink.manufacturingProcess.append('cupdropper')
            if drink.ingredients is not None:
                drink.manufacturingProcess.append('ingredients')
            if drink.ice > 0:
                drink.manufacturingProcess.append('ice')
            if drink.drink is not None:
                drink.manufacturingProcess.append(drink.drink)
            drink.manufacturingProcess.append('sealer')
            self.drink_id += 1 
            self.waitingList.append(drink)
        
        if self.cupdropper.status == 'available':
            self.fromWaitingToProcess()
            return
        else:
            return
            

    def stationNotification(self,msg):
        return

    def armNotification(self,msg):
        return

    def fromWaitingToProcess(self):
        target = self.waitingList.pop(0)
        target.nextMove = 'drop'
        self.processingList.append(target)
        return
    
