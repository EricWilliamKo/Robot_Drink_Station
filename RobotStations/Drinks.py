

class Drink:
    status = None
    ingredients = None
    sugar = 0
    ice = 0
    drink = None

    def __init__(self, **entries):
        self.__dict__.update(entries)