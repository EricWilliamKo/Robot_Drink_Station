import time
from threading import Timer

class Station:


    def __init__(self,stationName):
        self.status = 'available'
        self.remain = 100
        self.drink = None
        self.stationName = stationName
        self.processing_id = None
    
    def register(self,notifyFunc):
        self.notifyFunc = notifyFunc

    def notify(self):
        print self.stationName,' done'
        self.status = 'available' 
        self.notifyFunc(self.stationName,self.processing_id)

    def work(self,vol):
        workFuncDic = {
            'cupdropper':self.drop,'ice':self.iceFilling,
            'ingredients':self.ingredientsFilling,'black_tea':self.blackTeaFilling,
            'wm_tea':self.wmTeaFilling,'sealer':self.seal }
        workFuncDic[self.stationName](vol)

    def drop(self,vol):
        print 'cup dropping'
        Timer(1,self.notify).start()
        return

    def blackTeaFilling(self,vol):
        print 'black tea filling ',str(vol)
        Timer(1,self.notify).start()
        return

    def wmTeaFilling(self,vol):
        print 'winter melon tea filling ',str(vol)
        Timer(1,self.notify).start()
        return

    def iceFilling(self,vol):
        print 'ice filling ',str(vol)
        Timer(1,self.notify).start()
        return

    def ingredientsFilling(self,vol):
        print 'ingredients filling ',str(vol)
        Timer(1,self.notify).start()
        return

    def seal(self,vol):
        print 'sealing cup'
        Timer(1,self.notify).start()
        return