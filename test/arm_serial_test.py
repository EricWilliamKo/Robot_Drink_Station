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
    cmd = '#1P1900T1500'
    cmd2 = '#1P1500T1000'
    moveArm(cmd)
    wait = float(cmd[cmd.index('T')+1:])/1000
    time.sleep(wait)
    moveArm(cmd2)
    