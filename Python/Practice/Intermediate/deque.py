#deque
from collections import deque

#use deque instead of list b/c it is faster to add 
#use list instead of deque b/c it is faster to iterate

d = deque("hello")
#d = deque("hello", maxlen=5) #used to keep a maximum length of the deque
#d = list("hello")
d.appendleft('4')
d.append(5)
print(d)
d.pop() # removes right most
d.popleft() # remove left most
#d.clear() removes everything
add = [1,2,3]
d.extend('456')
d.extendleft(add)
print(d)
d.rotate(-3) # rotates left
print(d)
d.rotate(3) # rotates right
print(d)



