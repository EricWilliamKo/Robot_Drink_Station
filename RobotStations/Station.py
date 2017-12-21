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
        if self.stationName == 'cupdropper':
            self.status = 'available' 
        else:
            self.status = 'done'
        self.notifyFunc(self.stationName,self.processing_id)

    def getLocation(self):
        locationDic = {'cupdropper':'S1','ingredients':'S2','ice':'S3','black_tea':'S4',
                    'wm_tea':'S5','sealer':'S6'}
        return locationDic[self.stationName]

    def work(self,vol):
        workFuncDic = {
            'cupdropper':self.drop,'ice':self.iceFilling,
            'ingredients':self.ingredientsFilling,'black_tea':self.blackTeaFilling,
            'wm_tea':self.wmTeaFilling,'sealer':self.seal }
        self.status == 'working'
        workFuncDic[self.stationName](vol)

    def drop(self,vol):
        print 'cup dropping'
        t = Timer(1,self.notify)
        t.daemon = True
        t.start()
        return

    def blackTeaFilling(self,vol):
        print 'black tea filling ',str(vol)
        t = Timer(1,self.notify)
        t.daemon = True
        t.start()
        return

    def wmTeaFilling(self,vol):
        print 'winter melon tea filling ',str(vol)
        t = Timer(1,self.notify)
        t.daemon = True
        t.start()
        return

    def iceFilling(self,vol):
        print 'ice filling ',str(vol)
        t = Timer(1,self.notify)
        t.daemon = True
        t.start()
        return

    def ingredientsFilling(self,vol):
        print 'ingredients filling ',str(vol)
        t = Timer(1,self.notify)
        t.daemon = True
        t.start()
        return

    def seal(self,vol):
        print 'sealing cup'
        t = Timer(1,self.notify)
        t.daemon = True
        t.start()
        return