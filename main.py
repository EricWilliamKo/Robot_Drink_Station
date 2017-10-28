"""
"""

import os.path
import cherrypy
import json
import time

class RobotStationServer():

    @cherrypy.expose
    def index(self):
        return 'hello world'

    @cherrypy.expose
    def order(self):
        return 'order status'

severconf = os.path.join(os.path.dirname(__file__), 'cherrypy.conf')

if __name__ == '__main__':
    # CherryPy always starts with app.root when trying to map request URIs
    # to objects, so we need to mount a request handler root. A request
    # to '/' will be mapped to HelloWorld().index().
    cherrypy.quickstart(RobotStationServer(), config=severconf)