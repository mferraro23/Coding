#Strings: ordered, immutable, text representation

#string declaration
my_string = "Hello World"
print(my_string)

#use \ to escape string and allow for another quote
print('i\'m a programmer')

#use """ """ for multi line text 
#commonly used for documentation in programs
"""
This is 
multi line
text
"""

#get the char at an index
my_string = "hello world"
char = my_string[0]
#use -2 for second to last and -1 for last
print(char)

#make substring using [start_index:end_index]
subString = my_string[1:5]
print(subString)
#[:] goes beginning to end
#[::1] takes every char using step
#[::2] takes every other char using step
#[::-1] reverses the string

#string concate
greeting = 'Hello'
name = 'Mike'
sentance = greeting + name
print(sentance)# returns with no space in between 

#iterate over string 
for i in greeting:
    print(i)
#check if char in string 
if 'e' in greeting:
    print("Yes")
else:
    print('no')
#check for substring as well
if 'ell' in greeting:
    print('Yes')
else:
    print('no')

#use strip(to remove whitespace)
my_string = '     Hello World    '
print(my_string)
my_string = my_string.strip() #need to reassign to self
#this is becuase it is immutable
print(my_string)

#convert every char to uppercase
print(my_string.upper())
#convert every char to lowercase
print(my_string.lower())
#for both of these you also cannot use them alone
#in a statement. to keep them all upper or all lower
#you need to reassign 

#check if string starts with char or substring
#returns boolean value 
print(my_string.startswith('Hello'))
#check if string ends with char or substring
#returns boolean value
print(my_string.endswith('World'))

#find() used to find index of string or char
print(my_string.find('l'))
print(my_string.find('He'))
#not finding the char returns -1

#count the occurances of a char in a string
print(my_string.count('l'))

#replace char or substring in string
#returns new string so set assignment
print(my_string.replace('World', 'Universe'))

#convert to list
my_string = 'how are you today'
my_list = my_string.split()
#default argument is space
print(my_list)
#convert back to string 

#puts whatever is in between '' as what the split is
new_String = ' '.join(my_list)
print(new_String)

#create list with 6 strings
my_list = ['a'] *6
#then turn list into a string
from timeit import default_timer as timer
#bad method
start = timer()
my_string = ''
for i in my_list:
    my_string += i
print(my_string)
stop = timer()
print(stop-start)
#good method
start = timer()
my_string = ''.join(my_list)
print(my_string)
stop = timer()
print(stop-start)
#cleaner and much faster than above

#format string
# %, .format(), f-strings
#old
var = 'tom'
my_string = "the variable is %s" % var
print(my_string)
#this fills the place holder %s with the variable
#use %s for string %d for decimal and %f for floating point
#default is 6 decimal points
#can specify by doing %.2f
var = 3.23445
my_string = "the variable is %.2f" % var
print(my_string)

#new method 
#.format(method)
var = 3.23353
var2 = 6
my_string = "the var is {}".format(var)
print(my_string)
#can specify decimal place using {:.numf}
my_string = "the var is {:.2f} and {}".format(var,var2)

#new method
#f-strings
my_string = f"the var is {var} and {var2}"
#this is the best option
#faster, better readability
#operates at runtime
print(my_string)

