"""
"""

import os.path
import cherrypy
import json
import time
from RobotStations.Drinks import Drink
from RobotStations.Arm import Arm
from ProcessController import ProcessController

class RobotStationServer():
    arm = Arm()
    processController = ProcessController()
    orderList = []

    @cherrypy.expose
    def index(self):
        return 'welcome to virtuoso robot drink station'

    @cherrypy.expose
    @cherrypy.tools.json_in()
    def order(self):
        orderdata = cherrypy.request.json
        for drinkinfo in orderdata['orderList']:
            drink = Drink(**drinkinfo)
            self.orderList.append(drink)

        return 'order recivied'

severconf = os.path.join(os.path.dirname(__file__), 'cherrypy.conf')

if __name__ == '__main__':
    cherrypy.quickstart(RobotStationServer(), config=severconf)