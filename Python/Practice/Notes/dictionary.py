#Dictionary: Key-Value pairs, Unordered, Mutable

#FORMAT 
#KEY: VALUE
#declare dictionary using dictionary format
myDict = {"name": "Max", "age": 28, "city": "New York"}
print(myDict)

#declare dictionary using dict()
myDict2 = dict(name="Mary", age=27, city="Boston")
print(myDict2)

#accessing Value using the KEY
value = myDict2["name"]
print(value)

#add or change items after creation
myDict["email"] = "max@xyz.com"
print(myDict)
#if key exists then only value changes
myDict["email"] = "michael@xyz.com"
print(myDict)
#delete KEY and it's VALUE using del
del myDict["email"]
print(myDict)
#or 
myDict.pop("age")
print(myDict)
#or 
myDict.popitem() #removes last inserted item
print(myDict)


#check
if "name" in myDict:
    print(myDict["name"])
else:
    print("Not in")

#can also use a try except
try:
   print(myDict["age"])
except:
    print("Not in it")

#iterate through dict to find all keys
for key in myDict:
    print(key)
#or
for key in myDict.keys():
    print(key)
#or
key = myDict.keys()
print(key)
#iterate through dict to find values
for value in myDict.values():
    print(value)

#both in one loop using items()
for key, value in myDict.items():
    print(key, value)

#copy dict
myDict_copy = myDict
#modifying copy will also modify the original
myDict_copy["email"] = "maxxyz@gmail.com"
print(myDict)
print(myDict_copy)
#to completely copy, use copy()
myDict_copy = myDict.copy()
myDict_copy["age"] = 26
print(myDict)
print(myDict_copy)
#merge dict
#overwrite existing key values 
#add new key values
myDict = {"name": "Max", "age": 28, "city": "New York"}
myDict2 = dict(name="Mary", age=27, city="Boston")
myDict.update(myDict2)
print(myDict)

#you can use any immutable elements as a key
myDict = {3:9, 6:36, 9:81}
print(myDict)
#when using numbers, you cannot use the index
#to access the values you need to use the key itself
value = myDict[3]
print(value)#prints 9

#can use tuple as a key 
myTuple = (8,7)
myDict = {myTuple: 15}#tuple as key with sum as value
print(myDict)
#you cannot use a list becuase it is mutable
#end