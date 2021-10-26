#filter functions

def add7(x):
    return x+7

def isOdd(x):
    return True

a= [1,2,3,4,5,6,7,8,9,10]
c= list(map(add7, filter(isOdd, a)))
print(c)

