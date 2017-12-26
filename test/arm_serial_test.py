#!/usr/bin/env python
import serial
import time
import threading
from threading import Thread

armSerial = serial.Serial("/dev/arm",115200)

def moveArm():
    cmd = '#1P1500T1000\r\n#1P1500T1000\r\n'
    armSerial.write(cmd)
    print cmd

def sendCmd(cmd):
    end = '\r\n'
    armSerial.write(cmd+end)

def move2():
    end = '\r\n'
    cmd = '#1P1800T1000\r\n'
    cmd2 = '#1P1500T1000\r\n'
    armSerial.write(cmd+end)
    print cmd
    time.sleep(1)
    armSerial.write(cmd2+end)
    print cmd2
    time.sleep(1)
    print 'done'

class Move(Thread):
    def run(self):
        end = '\r\n'
        cmd = '#1P1800T1000\r\n'
        cmd2 = '#1P1500T1000\r\n'
        armSerial.write(cmd+end)
        print cmd
        time.sleep(1)
        armSerial.write(cmd2+end)
        print cmd2
        time.sleep(1)
        print 'done'




if __name__ == '__main__':
    time.sleep(1)
    # Move().start()
    # move2().start()
    # moveArm()

    serialThread = threading.Thread(target = move2)
    serialThread.daemon = True
    serialThread.start()

    time.sleep(5)

    
    