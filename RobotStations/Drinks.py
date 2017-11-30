

class Drink:

    def __init__(self, **entries):
        self.nextMove = None
        self.ingredients = 0
        self.sugar = 0
        self.ice = 0
        self.black_tea = 0
        self.wm_tea = 0
        self.id = None
        self.manufacturingProcess = []
        self.__dict__.update(entries)

    def getVolume(self,station):
        volumeDic = {'ingredients':self.ingredients,'ice':self.ice,
                        'black_tea':self.black_tea,'wm_tea':self.wm_tea}
        return volumeDic[station]