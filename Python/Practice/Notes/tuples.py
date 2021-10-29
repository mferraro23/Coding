# Tuple: ordered, immutable, allows duplicate elements

#declare tuple
#parenthesis are optional
myTuple = ("Max", 28, "Boston")
print(myTuple)
#to have a signle tuple recognized as a tuple
myTuple = ("Michael") # will return as a string
#need ',' at the end to show its continuing
myTuple = ("Michael",)
print(myTuple)

#can use tuple() to create a tuple from a list
myTuple = tuple(["Chloe", "Michael", "Kevin"])
print(myTuple)

#set items = to index's
item = myTuple[0] #start at 0
print(item)
#can specify -n,
#-1 is the last -2 is the second to last and so on
item = myTuple[-2]
print(item)

#2 ways to iterate over tuple
for i in myTuple:
    print(i)
for i in range(len(myTuple)):
    print(myTuple[i])

#can check if element is in tuple

if "Michael" in myTuple:
    print("Yes")
else:
    print("No")

#get number of elements using len()
myTuple= ('a','p','p','l','e')
print(len(myTuple))
#get number of same occurances in tuple
print("num of 'p':", myTuple.count('p'))
#get index of first occurance of param passed
print(myTuple.index('p'))

#convert tuple to list using list() function
myList = list(myTuple)
print(myList)
#convert back
myTuple2 = tuple(myList)
print(myTuple2)

#splicing
a = (1,2,3,4,5,6,7,8,9,10)
#syntax [start:stop]
b = a[2:5]
#also step
b = a[::1] #begining to end with step 1
b = a[::-1] #trick to reverse tuple

#assign elements to variables from tuple
myTuple = "Max", 28, "Boston"
#num elements here must match amount in tuple
name, age, city = myTuple
print(name, age, city)
#can put multiples using *
myTuple = (0,1,2,3,4,)
i1, *i2, i3 = myTuple 
print(i1) #first element 
print(i2) #last element
print(i3) #everything else

#showing that tuples may be more efficent and faster 
#for larger data sets and creating/iterating through
#them, use tuple unless you need a mutable data type

import sys
import timeit
my_List = [0,1,2,"hello", True]
my_Tuple = (0,1,2,"hello", True)
print(sys.getsizeof(my_List), "bytes")
print(sys.getsizeof(myTuple), "bytes")
print(timeit.timeit(stmt="[0,1,2,3,4,5]", number=1000000))
print(timeit.timeit(stmt="(0,1,2,3,4,5)", number=1000000))
#end