from RobotStations.Drinks import Drink

class Locker:

    def __init__(self,number,serLED):
        self.status = 'empty'
        self.lockerNumber = number
        self.drink = Drink()
        self.serialLED = serLED

    def isEmpty(self):
        if self.status == 'empty':
            return True
        else:
            return False

    def storeDrink(self,drink):
        self.drink = drink
        self.status = 'occupied'
        print 'drink locked id = %d'%(drink.id)
        return

    def unlockDrink(self):
        ledDic = {1:'72',2:'74',3:'76'}
        cmd = 'S' + ledDic[self.lockerNumber] + 'E'
        self.serialLED.write(cmd)
        self.drink_id = None
        self.status = 'waiting'
        print 'unlock locker %d'%(self.lockerNumber)
        return

    def emptyNow(self):
        ledDic = {1:'71',2:'73',3:'75'}
        cmd = 'S' + ledDic[self.lockerNumber] + 'E'
        self.serialLED.write(cmd)
        self.status = 'empty'
        return

    def getDrinkid(self):
        return self.drink.id

    def getLocation(self):
        locationDic = {1:'L1',2:'L2',3:'L3'}
        return locationDic[self.lockerNumber]
