#Sets: Unordered, mutable, no duplicates

#declare a set
mySet = {1,2,3,4}
print(mySet)
#declare a set with duplicates will return the set
#with no duplicates
mySet = {1,1,1,2,2,2,3,3,3,3,3,4,4}
print(mySet)

#can declare a set with a list 
mySet = set([1,2,3,4])
print(mySet)
#declare a set with a string
mySet = set("Hello")  # order is not important to a set
print(mySet) 
#nice trick to find how many different
#chars are in your word

#empty set needs to be done with set() method 
#if done as myset = {} it is recognized as a dict
mySet = {}
print(type(mySet))
mySet = set()
print(type(mySet))

#add elements to set
mySet.add(1)
mySet.add(2)
mySet.add(3)
print(mySet)
#remove elements
mySet.remove(3)
print(mySet)

#discard() same as remove but wont raise exception
#if element was not found 

mySet.discard(3) 
#since already removed it should raise an exception
#but since we used discard() and not remove() it wont

#pop returns first value in set and removes it
item = mySet.pop()
print(item)
print(mySet)

#iterate over set
for x in mySet:
    print(x)
#check if item is in set
if 2 in mySet:
    print("Yes")
else:
    print("No")

#union and intersection
#union combines elements from 2 sets without
#duplication
odds = {1,3,5,7,9}
evens = {0,2,4,6,8}
primes = {2,3,5,7}
#union
u = odds.union(evens)
print(u)
#intersection only prints elements found in both
#sets
i = odds.intersection(primes)
print(i)

#returns all values that are in set a that are 
#not in set b
setA = {1,2,3,4,5,6,7,8,9}
setB = {1,2,3,10,11,12}
diff = setA.difference(setB)
print(diff)

#symetric difference method returns all elements from
#sets a and b but not the ones that are shared
sym_diff = setA.symmetric_difference(setB)
print(sym_diff)
#these will not modify the new sets
#you can modify the sets in place
#updates the set with elements found in the other set 
setA.update(setB)
print(setA)

#updates the set by keeping the values only
# found in both sets
setA.intersection_update(setB)
print(setA)

#updates the set by removing the elements that are
#also found in the other set
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}
setA.difference_update(setB)
print(setA)

#updates the set that only keeps the difference
#between the two
setA.symmetric_difference_update(setB)
print(setA)

#subset
#determines if the first set is a sub set of the
#second set listed. This means that the first set
#contains every element in the second set
setA = {1, 2, 3, 4, 5, 6}
setB = {1, 2, 3}
print(setB.issubset(setA)) #returns true

#superset
#a super set returns true if the first set contains
#all the elements from the second set
print(setA.issuperset(setB))

#disjoint
#returns true if they share no common elements 
#returns false if they share at least one common
#element
setC = {7,8}
print(setA.isdisjoint(setC))

#copy sets
#be careful because using 
# newSet = setA
#will change original
#to make actual copy use .copy() method 
#or
#use set() method
newSet1 = setA.copy()
newSet2 = set(setA)

#frozenset() method
#immutable version of normal set
a = frozenset([1,2,3,4,5])
print(a)
#you cannot change this after creation
#end