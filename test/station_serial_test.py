#!/usr/bin/env python
import serial
import time

armSerial = serial.Serial("/dev/mega_station",9600)

def stationWork(cmd):
    start = 'S'
    end = 'E'
    command = start+cmd+end
    armSerial.write(command)
    # armSerial.write('S72ES74E')
    print command


if __name__ == '__main__':
    time.sleep(2)
    cmd = '11'
    cmd2 = '21'
    cmd3 = '33'
    cmd4 = '43'
    cmd5 = '54'
    cmd6 = '72'
    cmd7 = '74'
    cmd8 = '76'
    # stationWork(cmd)
    # stationWork(cmd2)
    # stationWork(cmd3)
    # stationWork(cmd4)
    # stationWork(cmd5)
    stationWork(cmd6)
    stationWork(cmd7)
    stationWork(cmd8)
