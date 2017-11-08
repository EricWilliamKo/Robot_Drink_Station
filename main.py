"""
"""

import os.path
import cherrypy
import json
import time
from Drinks import Drink

class RobotStationServer():
    orderList = []

    @cherrypy.expose
    def index(self):
        return 'welcome to virtuoso robot drink station'

    @cherrypy.expose
    @cherrypy.tools.json_in()
    def order(self):
        orderdata = cherrypy.request.json
        for drinkinfo in orderdata['orderList']:
            drink = Drink(**orderdata)
            self.orderList.append(drink)

        return 'order recivied'

severconf = os.path.join(os.path.dirname(__file__), 'cherrypy.conf')

if __name__ == '__main__':
    # CherryPy always starts with app.root when trying to map request URIs
    # to objects, so we need to mount a request handler root. A request
    # to '/' will be mapped to HelloWorld().index().
    cherrypy.quickstart(RobotStationServer(), config=severconf)