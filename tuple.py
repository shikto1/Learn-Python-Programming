"""
A tuple is a collection which is ordered and unchangeable.
In Python tuples are written with round brackets ().

Read only
"""

names = ("tannima", "onnima", "naida")
print(names)

# create with constructor:
fruits = tuple(("banana", "apple"))
print(fruits)

# Accessing tuple item is as like as list // As like as list
print(names[0])
print(names[:2])
print(names[1:])
print(names[1:3])
print(names[-1])
print(names[-2])

# change tuple values is as list ***** Not like as list.
'''
 Once a tuple is created, you cannot change its values. 
 Tuples are unchangeable, or immutable as it also is called.
 But there is a workaround. You can convert the tuple into a list,
 change the list, and convert the list back into a tuple.
 '''
nameList = list(names)
nameList[0] = "Shshir"
names = tuple(nameList)
print(names)

# Loop through a tuple // As like as list
for name in names:
    print(name)

# Check item is exit or not  // As like as list
if "tannima" in names:
    print("Exists")
else:
    print("Not Exists")

# Tuple length:
print(len(names))

# Remove from tuple


# Join two tuple
tuple1 = (1, 2)
tuple2 = (3, "ss")
tuple3 = tuple1 + tuple2
print(tuple3)

# Tuple in tuple
t = ((1, 2, 3), 4, 5)
print(t)

# Get Nested tuple value
firstTupleValue = t[0]
print(firstTupleValue)
firstValueOfTupleValue = firstTupleValue[0]
print(firstValueOfTupleValue)

# Another way of getting nested tuple value
print(t[0][0])

"""
List vs Tuple
-------------------------------------------------------------------
** Lists are surrounded by square brackets [] and Tuples are surrounded by parenthesis ()

** List is mutable (changeable) but tuple is immutable (non-changeable)
 
** To change in tuple. The trick is: convert tuple to list then append new item, 
   then again convert the list to tuple.
   
** Tuple consume less memory than list for its fixed size.

** Iteration is comparativly faster in tuple than list
   
** All other functions are same both for list and tuple 

** List has more functionality than the tuple

** List is better for performing operation

"""