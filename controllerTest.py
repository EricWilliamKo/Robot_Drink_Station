from processController import ProcessController
import json
from RobotStations.Drinks import Drink

pc = ProcessController()
drink1 = Drink()
drink2 = Drink()


drink1.black_tea = 10
drink1.wm_tea = 0
drink1.ingredients = 5
drink1.ice = 5
drink1.sugar = 3

drink2.black_tea = 1
drink2.wm_tea = 10
drink2.ingredients = 3
drink2.ice = 7
drink2.sugar = 0

drinkList = [drink1,drink2]

if __name__ == '__main__':
    pc.getorder(drinkList)