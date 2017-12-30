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
    time.sleep(7)
    cmd = '81'
    cmd2 = '21'
    cmd3 = '71'
    cmd4 = '73'
    cmd5 = '75'
    cmd6 = '72'
    cmd7 = '74'
    cmd8 = '76'
    # stationWork(cmd)
    # stationWork(cmd2)
    # stationWork(cmd3)
    # stationWork(cmd4)
    # stationWork(cmd5)
    stationWork(cmd)
    # stationWork(cmd7)
    # stationWork(cmd8)
    # time.sleep(5)
    # stationWork(cmd3)
    # stationWork(cmd4)
    # stationWork(cmd5)
