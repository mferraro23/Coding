#optional parameters 
class car(object):
    def __init__(self, make, model, year, condition='new', miles='0'):
        self.make = make
        self.model = model
        self.year = year
        self.condition = condition
        self.miles = miles

    def printScreen(self, showAll=True):
        if showAll:
            print("My car is a %s %s %s. It is %s with %s miles." %(self.year, self.make, self.model, self.condition, self.miles))
        else:
            print("My %s %s %s is trash" %(self.year, self.make, self.model))

whip = car('BMW', 'M5 CS', '2022')
whip.printScreen(True)


