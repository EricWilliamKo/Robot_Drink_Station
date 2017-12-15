"""
"""

import os.path
import cherrypy
import json
import time
from random import randint
from RobotStations.Drinks import Drink
from processController import ProcessController

class RobotStationServer:

    def __init__(self):
        self.processController = ProcessController()

    @cherrypy.expose
    def index(self):
        return 'welcome to virtuoso robot drink station'

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def order(self):
        # print 'get somthing'
        orderList = []
        order_id = randint(0,9999)
        orderdata = cherrypy.request.json
        print orderdata
        for drinkinfo in orderdata['orderList']:
            drink = Drink(**drinkinfo)
            drink.order_id = order_id
            orderList.append(drink)
            print drink.__dict__

        self.processController.getorder(orderList)
        self.processController.lockerManager.addProcessingOrder(order_id)
        print orderList
        return {'response':'Order recivied!! Your order id is %d'%order_id}

    @cherrypy.expose
    def getProcess(self):
        info = 'processing list = '
        for drink in self.processController.getProcessingList():
            info += str(drink.__dict__)
            
        return info
    
    @cherrypy.expose
    def close(self):
        self.processController.lockerManager.disConnectMega()
        return 'serial closed'



severconf = os.path.join(os.path.dirname(__file__), 'cherrypy.conf')

if __name__ == '__main__':
    cherrypy.quickstart(RobotStationServer(), config=severconf)