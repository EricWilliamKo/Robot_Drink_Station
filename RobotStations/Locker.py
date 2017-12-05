

class Locker:

    def __init__(self,number):
        self.status = 'empty'
        self.lockerNumber = number
        self.drink_id = None

    def isEmpty(self):
        if self.status == 'empty':
            return True
        else:
            return False

    def storeDrink(self,drink_id):
        self.drink_id = drink_id
        self.status = 'occupied'
        print 'drink locked id = %d'%(drink_id)
        return

    def unlockDrink(self):
        self.drink_id = None
        self.status = 'empty'
        print 'unlock locker %d'%(self.lockerNumber)
        return

    def getDrinkid(self):
        return self.drink_id

    def getLocation(self):
        locationDic = {1:'L1',2:'L2',3:'L3'}
        return locationDic[self.lockerNumber]