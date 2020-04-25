"""
Python Collections (Arrays)
There are four collection data types in the Python programming language:

// Duplicate members allowed: List, Tuple
# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

// No duplicate members allowed: Set, Dictionary
# Set is a collection which is unordered and unindexed. No duplicate members.
# Dictionary is a collection which is unordered, changeable and indexed. No duplicate members

"""
"""
[] = list : mutable, allow duplicate value
() = tuple immutable, allow duplicate value
{} = dictionary {key:value, key:value} : mutable, no duplicate keys
     Set { value1, value, value3 } : mutable, no duplicate values
"""

# Creating Collection
listExample = [1, 2, 3]
tupleExample = (1, 2, 3)
dictionaryExample = {0: 1, 1: 1, 2: 2}
setExample = {1, 2, 3}

print(listExample)
print(tupleExample)
print(dictionaryExample)
print(setExample)

# creating collection with construction
listExample = list((1, 2, 3))
tupleExample = tuple((1, 2, 3))
dictionaryExample = dict(brand="Ford", model="Mustang", year=1964)
setExample = set((1, 2, 3))

print(listExample)
print(tupleExample)
print(dictionaryExample)
print(setExample)
