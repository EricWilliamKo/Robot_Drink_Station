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
        #reflection make every path bidirectional
        ('P1','S1',1),('P2','S2',1),('P3','S3',1),('P4','S4',1),('P5','S5',1),('P5I','S5I',1), 
        ('P6','L1',1),('P7','L2',1),('P8','L3',1), 
        ('P2','P1',1),('P2','P1',1),('P3','P2',1),('P4','P3',1),('P5','P4',1), 
        ('P7','P6',1),('P8','P7',1), 
        ('P1','P0',3),('P2','P0',3),('P3','P0',3),('P4','P0',3), 'P5','P0',3),('P5I','P0',3), 
        ('P6','P0',3),('P7','P0',3),('P8','P0',3)
    ]

    def register(self,sub):
        self.subsciber = sub

    def notifyController(self,msg):
        self.subsciber(msg)

    def grab():
        return

    def moveToNext(terminal):
        
        

