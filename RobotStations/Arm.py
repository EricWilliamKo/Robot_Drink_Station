import serial
import time
from threading import Timer

class Arm:
    armSerial = serial.Serial('/dev/arm',115200)
    position = None
    status = None

    edges = [
        ('S1','P1',1),('S2','P2',1),('S3','P3',1),('S4','P4',1),('S5','P5',1),('S5I','P5I',1),
        ('L1','P6',1),('L2','P7',1),('L3','P8',1),
        ('P1','P2',1),('P1','P2',1),('P2','P3',1),('P3','P4',1),('P4','P5',1),
        ('P6','P7',1),('P7','P8',1),
        ('P0','P1',3),('P0','P2',3),('P0','P3',3),('P0','P4',3),('P0','P5',3),('P0','P5I',3),
        ('P0','P6',3),('P0','P7',3),('P0','P8',3),
    ]

    def register(self,sub):
        self.subsciber = sub

    def notifyController(self,msg):
        self.subsciber(msg)

    # def cupdropper_ingredients(self):
    #     self.armSerial.write('')
    #     Timer(1,self.notifyController('ingredients reached')).start()

    # def cupdropper_ice(self):
    #     self.armSerial.write('')
    #     Timer(1,self.notifyController('ice reached')).start()

    # def ingredients_ice(self):
    #     self.armSerial.write('')
    #     Timer(1,self.notifyController('ice reached')).start()

    # def ice_fourseason(self):
    #     self.armSerial.write('')
    #     Timer(1,self.notifyController('fourseason reached')).start()

    # def ice_blackTea(self):
    #     self.armSerial.write('')
    #     Timer(1,self.notifyController('black tea reached')).start()

    # def fourseason_sealer(self):
    #     self.armSerial.write('')
    #     Timer(1,self.notifyController('sealer reached')).start()

    # def blackTea_sealer(self):
    #     self.armSerial.write('')
    #     Timer(1,self.notifyController('sealer reached')).start()
        
    # def sealer_locker1(self):
    #     self.armSerial.write('')
    #     Timer(1,self.notifyController('locker 1 reached')).start()

    # def sealer_locker2(self):
    #     self.armSerial.write('')
    #     Timer(1,self.notifyController('locker 2 reached')).start()

    # def sealer_locker3(self):
    #     self.armSerial.write('')
    #     Timer(1,self.notifyController('locker 3 reached')).start()
    