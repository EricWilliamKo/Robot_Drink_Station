from RobotStations.Drinks import Drink

drink1 = Drink()
drink2 = Drink()

drink1.id = 1
drink2.id = 2

drink1.black_tea = 100

a = [drink1,drink2]
adic = {'a':drink1,'b':drink2}

yeah = adic['a']


# yo = next((drink for drink in a if drink.id == 1), None)
# print yo
# yo.ingredients = 'fucking shit'
# print drink1.ingredients
# print drink2.ingredients
# print a[0].ingredients

print yeah.getVolume('black_tea').__class__

