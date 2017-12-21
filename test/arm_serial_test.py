#!/usr/bin/env python
import serial
import time

armSerial = serial.Serial("/dev/arm",115200)

def moveArm(cmd):
    end = '\r\n'
    armSerial.write(cmd+end)
    print cmd


if __name__ == '__main__':
    time.sleep(1)
    cmd = '#1P800#2P1500#3P2300#4P800#5P1500#6P1350T3000'
    cmd2 = '#1P800#2P1000#3P2300#4P800#5P1500#6P1350T3000'
    moveArm(cmd)
    wait = float(cmd[cmd.index('T')+1:])/1000
    time.sleep(wait)
    moveArm(cmd2)
    