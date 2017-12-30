import time
from threading import Timer

class Station:


    def __init__(self,stationName,ser):
        self.status = 'available'
        self.remain = 100
        self.drink = None
        self.stationName = stationName
        self.processing_id = None
        self.stationSerial = ser
    
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
        self.stationSerial.write('S11E')
        t = Timer(1,self.notify)
        t.daemon = True
        t.start()
        return

    def blackTeaFilling(self,vol):
        wtime = 1.0
        if vol <= 10 and vol > 8:
            self.stationSerial.write('S41E')
            wtime = 28
        elif vol <= 8 and vol > 5:
            self.stationSerial.write('S42E')
            wtime = 19
        elif vol <= 5 and vol > 3:
            self.stationSerial.write('S43E')
            wtime = 15
        elif vol <= 3 and vol > 1:
            self.stationSerial.write('S44E')
            wtime = 10

        print 'black tea filling ',str(vol)
        t = Timer(wtime,self.notify)
        t.daemon = True
        t.start()
        return

    def wmTeaFilling(self,vol):
        wtime = 1.0
        if vol <= 10 and vol > 8:
            self.stationSerial.write('S51E')
            wtime = 28
        elif vol <= 8 and vol > 5:
            self.stationSerial.write('S52E')
            wtime = 19
        elif vol <= 5 and vol > 3:
            self.stationSerial.write('S53E')
            wtime = 15
        elif vol <= 3 and vol > 1:
            self.stationSerial.write('S54E')
            wtime = 10
            
        print 'winter melon tea filling ',str(vol)
        t = Timer(wtime,self.notify)
        t.daemon = True
        t.start()
        return

    def iceFilling(self,vol):
        if vol == 10:
            self.stationSerial.write('S39E')
        elif vol == 5:
            self.stationSerial.write('S33E')

        print 'ice filling ',str(vol)
        t = Timer(2,self.notify)
        t.daemon = True
        t.start()
        return

    def ingredientsFilling(self,vol):
        self.stationSerial.write('S21E')
        print 'ingredients filling ',str(vol)
        t = Timer(2,self.notify)
        t.daemon = True
        t.start()
        return

    def seal(self,vol):
        print 'sealing cup'
        t = Timer(1,self.notify)
        t.daemon = True
        t.start()
        return