# collections and counter
from collections import Counter

#containers
#list
#set
#dict
#tuple - inmuttable

#Types
#1 counter
#2 deque
#3 namedTuple ()
#4 orderDict
#5 default dict

#elements of list
#d = Counter(cats = 4, dogs=7)
#print(list(d.elements()))

#most common
#e = Counter(cars= 5, roads = 10)
#print(e.most_common(1))

c = Counter(a=4, b=2, c=0, d=-2)
d = Counter(['a', 'b', 'b', 'c'])

#c.subtract(d)
#print("removing similarities: ", c)
#c.update(d)
#print("adding it back: ", c)
#c.clear()
#print("Cleared 'C': ", c)
print("'C' original:", c)
print("'D' original:", d)

print("Adding them:", c+d)
print("Subtracting them:", c-d)
print("Intersection:", c & d) #intersection: min elements in each list
print("Union:", c | d) #union: max elements in each list


