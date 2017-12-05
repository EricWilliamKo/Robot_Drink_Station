"""
"""

import os.path
import cherrypy
import json
import time
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
    def order(self):
        orderList = []
        orderdata = cherrypy.request.json
        for drinkinfo in orderdata['orderList']:
            drink = Drink(**drinkinfo)
            orderList.append(drink)
            print drink.__dict__

        self.processController.getorder(orderList)
        print orderList
        return 'order recivied'

    @cherrypy.expose
    def getProcess(self):
        info = 'processing list = '
        for drink in self.processController.getProcessingList():
            info += str(drink.__dict__)
            
        return info


severconf = os.path.join(os.path.dirname(__file__), 'cherrypy.conf')

if __name__ == '__main__':
    cherrypy.quickstart(RobotStationServer(), config=severconf)