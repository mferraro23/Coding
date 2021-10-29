# map function
li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def func(x):
    return x**x

print(list(map(func, li)))

#print([func(x) for x in li])

# these 2 are the same, map is basically
# a fancy version of list comprehension 