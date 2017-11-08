import serial
import time
from threading import Timer

class Arm:
    armSerial = serial.Serial('/dev/arm',115200)
    position = None
    status = None

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
    