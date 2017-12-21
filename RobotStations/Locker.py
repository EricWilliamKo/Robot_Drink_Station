from RobotStations.Drinks import Drink

class Locker:

    def __init__(self,number):
        self.status = 'empty'
        self.lockerNumber = number
        self.drink = Drink()

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
        self.drink_id = None
        self.status = 'waiting'
        print 'unlock locker %d'%(self.lockerNumber)
        return

    def emptyNow(self):
        self.status = 'empty'
        return

    def getDrinkid(self):
        return self.drink.id

    def getLocation(self):
        locationDic = {1:'L1',2:'L2',3:'L3'}
        return locationDic[self.lockerNumber]
