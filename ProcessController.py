

class ProcessController():

    def __init__(self):
        self.waitingList = list()
        self.processingList = list()

    def getorder(neworders):
        for drink in neworders:
            drink.manufacturingProcess.append('cupdropper')
            if drink.ingredients is not None:
                drink.manufacturingProcess.append('ingredients')
            if drink.ice > 0:
                drink.manufacturingProcess.append('ice')
            if drink.drink is not None:
                drink.manufacturingProcess.append(drink.drink)
            drink.manufacturingProcess.append('sealer')
            waitingList.append(drink)

    def fromWaitingToProcess()
    
