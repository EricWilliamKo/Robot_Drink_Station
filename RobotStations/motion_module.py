import serial
import time
import threading
from threading import Thread

class MotionModule:

    def __init__(self):
        print 'motion module init'
        self.armSerial = serial.Serial('/dev/arm',115200)

    def toGoal(self,goal,wtime):
        moveDic = {'P0':self.toP0,'P1':self.toP1,'P2':self.toP2,'P3':self.toP3,'P4':self.toP4,
        'P5':self.toP5,'P6':self.toP6,'P6I':self.toP6I,'R1':self.toR1,
         'D0':self.toD0,'D1':self.toD1,'D2':self.toD2,'D3':self.toD3,'D3I':self.toD3I}
        moveDic[goal](wtime)

    def workingtime(self,cmdList):
        workingtime = 0.0
        for cmd in cmdList:
            wtime = float(cmd[cmd.index('T')+1:])/1000
            workingtime = workingtime +wtime
        return workingtime

    def toR1(self,wtime):
        pose = '#1P2030#2P1020#3P2300#4P800'
        cmd = pose + 'T' + wtime + '\r\n'
        self.sendCmdThread([cmd])

    def toD0(self,wtime):
        pose = '#1P1500#2P1600#3P1400#4P1600'
        cmd = pose + 'T' + wtime + '\r\n'
        self.sendCmdThread([cmd])

    def toD1(self,wtime):
        pose = '#1P1600#2P1200#3P2200#4P900'
        cmd = pose + 'T' + wtime + '\r\n'
        self.sendCmdThread([cmd])

    def toD2(self,wtime):
        pose = '#1P1600#2P1000#3P2300#4P800'
        cmd = pose + 'T' + wtime + '\r\n'
        self.sendCmdThread([cmd])

    def toD3(self,wtime):
        pose = '#1P963#2P1500#3P2475#4P828'
        cmd = pose + 'T' + wtime + '\r\n'
        self.sendCmdThread([cmd])

    def toD3I(self,wtime):
        pose = '#1P2082#2P1550#3P538#4P1949'
        cmd = pose + 'T' + wtime + '\r\n'
        self.sendCmdThread([cmd])

    def toP0(self,wtime):
        pose = '#1P1500#2P1500#3P1500#4P1500#5P1500#6P1500'
        cmd = pose + 'T' + wtime + '\r\n'
        self.sendCmdThread([cmd])

    def toP1(self,wtime):
        pose = '#1P1993#2P1020#3P2300#4P800'
        cmd = pose + 'T' + wtime + '\r\n'
        self.sendCmdThread([cmd])

    def toP2(self,wtime):
        pose = '#1P1735#2P1020#3P2300#4P800'
        cmd = pose + 'T' + wtime + '\r\n'
        self.sendCmdThread([cmd])

    def toP3(self,wtime):
        pose = '#1P1356#2P1020#3P2300#4P800'
        cmd = pose + 'T' + wtime + '\r\n'
        self.sendCmdThread([cmd])

    def toP4(self,wtime):
        pose = '#1P1093#2P1020#3P2300#4P800'
        cmd = pose + 'T' + wtime + '\r\n'
        self.sendCmdThread([cmd])

    def toP5(self,wtime):
        pose = '#1P963#2P1020#3P2300#4P800'
        cmd = pose + 'T' + wtime + '\r\n'
        self.sendCmdThread([cmd])

    def toP6(self,wtime):
        pose = '#1P963#2P1194#3P2475#4P828'
        cmd = pose + 'T' + wtime + '\r\n'
        self.sendCmdThread([cmd])

    def toP6I(self,wtime):
        pose = '#1P2082#2P1540#3P538#4P1949'
        cmd = pose + 'T' + wtime + '\r\n'
        self.sendCmdThread([cmd])

    

    def getCup(self):
        cmdList = [
            '#1P1993#2P1091#3P2310#4P910#5P1500T2000',
            '#6P1050T500',
            '#1P1993#2P1007#3P2111#4P984#5P1500T2000',
            '#6P1530T500'
            ]
        self.sendCmdThread(cmdList)
        return self.workingtime(cmdList)

    def pullCup(self):
        cmdList = [
            '#1P1993#2P1058#3P2150#4P1094#5P1500#6P1550T2000',
            '#1P1993#2P1179#3P2414#4P958#5P1500#6P1550T2000'
        ]
        self.sendCmdThread(cmdList)
        return self.workingtime(cmdList)

    def putS2(self):
        cmdList = [
            '#1P1735#2P1079#3P2300#4P848#5P1500#6P1550T1000',
            '#1P1765#2P935#3P1864#4P1131#5P1500#6P1550T1000',
            '#6P1050T500',
            '#1P1765#2P1040#3P2053#4P1040#5P1500T1000',
            '#1P1765#2P1150#3P2334#4P950#5P1500T1000'
        ]
        self.sendCmdThread(cmdList)
        return self.workingtime(cmdList)

    def getS2(self):
        cmdList = [
            '#1P1735#2P1079#3P2300#4P848#5P1500#6P1050T1000',
            '#1P1749#2P955#3P1886#4P1171#5P1500#6P1050T1000',
            '#6P1550T500',
            '#1P1765#2P993#3P2053#4P950#5P1500#6P1550T1500',
            '#1P1765#2P1170#3P2334#4P950#5P1500T1000',
            '#1P2030#2P1020#3P2300#4P800#6P1550T1000'
        ]
        self.sendCmdThread(cmdList)
        return self.workingtime(cmdList)

    def putS3(self):
        cmdList = [
            '#1P1356#2P1140#3P2408#4P828#5P1500#6P1550T1000',
            '#1P1356#2P1023#3P2125#4P1021#5P1500#6P1550T3000',
            '#6P1050T500',
            '#1P1356#2P1040#3P2231#4P911#5P1500#6P1050T1000',
            '#1P1356#2P1150#3P2334#4P950#5P1500T1000',
            '#1P2030#2P1020#3P2300#4P800#6P1550T4000'
        ]
        self.sendCmdThread(cmdList)
        return self.workingtime(cmdList)

    def getS3(self):
        cmdList = [
            '#1P1356#2P1140#3P2408#4P828#5P1500#6P1550T1000',
            '#1P1356#2P1023#3P2125#4P1021#5P1500#6P1050T3000',
            '#6P1550T500',
            '#1P1356#2P1085#3P2312#4P838#5P1500#6P1550T1000',
            '#1P1356#2P1150#3P2334#4P886#5P1500#6P1550T1000',
            '#1P2030#2P1020#3P2300#4P800#6P1550T4000'
        ]
        self.sendCmdThread(cmdList)
        return self.workingtime(cmdList)

    def putS4(self):
        cmdList = [
            '#1P1093#2P1133#3P2388#4P848#5P1500#6P1550T3000',
            '#1P1093#2P935#3P1864#4P1131#5P1500#6P1550T1000',
            '#6P1050T500',
            '#1P1093#2P1040#3P2053#4P1040#5P1500T1000',
            '#1P1093#2P1150#3P2334#4P950#5P1500T1000',
            '#1P2030#2P1020#3P2300#4P800#6P1550T3000'
        ]
        self.sendCmdThread(cmdList)
        return self.workingtime(cmdList)

    def getS4(self):
        cmdList = [
            '#1P1093#2P1079#3P2300#4P848#5P1500#6P1050T3000',
            '#1P1093#2P955#3P1886#4P1171#5P1500#6P1050T1000',
            '#6P1550T500',
            '#1P1093#2P993#3P2053#4P950#5P1500#6P1550T1500',
            '#1P1093#2P1170#3P2334#4P950#5P1500T1000',
            '#1P2030#2P1020#3P2300#4P800#6P1550T3000'
        ]
        self.sendCmdThread(cmdList)
        return self.workingtime(cmdList)

    def putS5(self):
        cmdList = [
            '#1P963#2P1133#3P2388#4P848#5P1500#6P1550T3000',
            '#1P963#2P960#3P2078#4P965#5P1500#6P1550T1000',
            '#6P1050T500',
            '#1P963#2P1033#3P2153#4P1000#5P1500#6P1050T700',
            '#1P963#2P1133#3P2388#4P848#5P1500T1000',
            '#1P2030#2P1020#3P2300#4P800#6P1550T3000'
        ]
        self.sendCmdThread(cmdList)
        return self.workingtime(cmdList)

    def getS5(self):
        cmdList = [
            '#1P963#2P1133#3P2388#4P848#5P1500#6P1050T3000',
            '#1P963#2P960#3P2078#4P965#5P1500#6P1050T1000',
            '#6P1550T500',
            '#1P963#2P1048#3P2153#4P1000#5P1500#6P1550T500',
            '#1P963#2P1133#3P2388#4P848#5P1500T1000',
            '#1P2030#2P1020#3P2300#4P800#6P1550T3000'
        ]
        self.sendCmdThread(cmdList)
        return self.workingtime(cmdList)

    def putS6(self):
        cmdList = [
            '#1P768#2P1194#3P2475#4P828#5P1500#6P1550T1000',
            '#1P768#2P1094#3P2381#4P828#5P1500#6P1550T1000',
            '#6P1050T500',
            '#1P768#2P1194#3P2475#4P828#5P1500T1000',
            '#1P963#2P1194#3P2475#4P828T1000'
        ]
        self.sendCmdThread(cmdList)
        return self.workingtime(cmdList)


    def getS6I(self):
        cmdList = [
            '#1P2082#2P1762#3P528#4P2117#5P1500#6P1050T2000',
            '#6P1550T500',
            '#1P2082#2P1764#3P558#4P2117#5P1500T1000',
            '#1P2082#2P1540#3P538#4P1949#5P1500#6P1550T1000'
        ]
        self.sendCmdThread(cmdList)
        return self.workingtime(cmdList)

    def putL1(self):
        cmdList = [
            '#1P1513#2P1815#3P882#4P1881#5P1500#6P1550T2000',
            '#1P1513#2P2038#3P1159#4P1758#5P1500#6P1550T1000',
            '#6P1050T500',
            '#1P1513#2P1806#3P768#4P2042#5P1500#6P1050T700'
        ]
        self.sendCmdThread(cmdList)
        return self.workingtime(cmdList)

    def putL2(self):
        cmdList = [
            '#1P1414#2P1806#3P768#4P2042#5P1500#6P1550T2000',
            '#1P1414#2P1891#3P1014#4P1763#5P1500#6P1550T700',
            '#1P1414#2P2117#3P1387#4P1604#5P1500#6P1550T700',
            '#6P1050T500',
            '#1P1414#2P1806#3P768#4P2042#5P1500#6P1050T700'
        ]
        self.sendCmdThread(cmdList)
        return self.workingtime(cmdList)

    def putL3(self):
        cmdList = [
            '#1P1319#2P1815#3P882#4P1881#5P1500#6P1550T2000',
            '#1P1319#2P2038#3P1159#4P1823#5P1500#6P1550T1000',
            '#6P1050T500',
            '#1P1319#2P1806#3P768#4P2042#5P1500#6P1050T700'
        ]
        self.sendCmdThread(cmdList)
        return self.workingtime(cmdList)

    

    def sendCmdThread(self,cmdList):
        cmdThread = threading.Thread(target=self.sendCmd,args=(cmdList,))
        cmdThread.daemon = True
        cmdThread.start()

    def sendCmd(self,cmds):
        end = '\r\n'
        for i, cmd in enumerate(cmds):
            print cmd
            self.armSerial.write(cmd)
            workingtime = float(cmd[cmd.index('T')+1:])/1000
            time.sleep(workingtime)
        
