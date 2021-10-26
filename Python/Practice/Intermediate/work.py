#attempt to do classes myself
class car(object):
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def showAll(self):
        currYear = 2021
        miles = currYear - self.year
        miles = miles * 10167

        print('My car is a %s %s %s. It has %s miles' %(self.year, self.make, self.model, miles))
    

myCar = car('BMW', '530i xDrive', 2017)
myCar.showAll()



    
