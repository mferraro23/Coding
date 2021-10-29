#Lists: ordered, mutable, allows duplicate elements

#declare a list with values already in it
myList = ["bannana", "cherry", "apple"]

#declare a list to add to later
myList2 = list() 

#can assing variables to item of list
#this sets item having the value bannana
item = myList[0] 
#using -1 refers to last item
item2 = myList[-1]
#using -2 refers to second to last item
#and so forth
item3 = myList[-2] 
print(item3)

#can change index values by accessing them
#directly as so
myList[-1] = "John"

#2 ways to iterate over list
#this
for i in range(len(myList)):
    print(myList[i])
#or this
for i in myList:
    print(i)

#check if something in list
if "bannana" in myList:
    print('yes')
else:
    print('no')
#can also use var
if item in myList:
    print('yes')
else:
    print('no')

#check the length of the list 
#returns the length from 1-n
#n-1 to get the index of each element in list
length = len(myList)

#append to list 
#adds to end of list
myList.append("lemon")
#to add at specific point
myList.insert(1, 'blueberry')
print(myList)
#remove and return last variable use pop
removedItem = myList.pop()
print("I removed", removedItem)
#remove specific item from list
removedItem = myList.remove('bannana')
#clear whole list, cannot set to variable
myList.clear()
print(myList)

myList = [4,3,5,2,1,6,9]
#sort list, based on letter or integer values
myList.sort()
#reverse list, used in conjunction with sort method
myList.reverse()
#these alter the original list 
#to preserve the original
#create a new list using sorted
newList = sorted(myList)
print(myList)
print(newList)
#easily create multiple of the same elements
myList = [0] * 5
print(myList)

#concate two lists together 
myList2 = [1,2,3,4,5]
newList = myList + myList2
print(newList)

#create a new list based off of input (slicing)
newList = [1,2,3,4,5,6,7,8,9,10]
a = newList[1:5] #[start: stop]
print(a)
#if start is not defined
a = newList[:5] #it starts at index 0 [newList[0]: 5]
#if stop is not defined
a = newList[1:]#it starts at the end of the list [1:(len(newList) - 1)]
#optional step index, taking item based off step 
#step of 1 will take every item
#step of 2 will take every 2nd item
#and so on
a = newList[1:5:2]
#this reads: start at index 1 end after index 4
#(at 5)
#but give every 2nd index
#[1], [3] are printed
print(a)
#trick to reverse is to use step -1
a = newList[::-1]
print(a)

#setting original to copy can be bad
#if changing the copy, it also changes the original
list_orig = ["bannana", "cherry", "apple"]
list_cpy = list_orig
list_cpy.append("lemon")
print(list_orig)
print(list_cpy)

#3 ways to make an actual copy of the list
#use the .copy() method
list_orig = ["bannana", "cherry", "apple"]
list_cpy = list_orig.copy()
list_cpy.append("lemon")
print(list_orig)
print(list_cpy)
#or
list_orig = ["bannana", "cherry", "apple"]
list_cpy = list(list_orig)
#or using slicing which i did on line 82

#list comprehension (another way to create a new list
# from an existing list)
a = [1,2,3,4,5,6]
b = [i*i for i in a]
#sytax: [(expression) for in loop over original list]
print(a)
print(b)
#end