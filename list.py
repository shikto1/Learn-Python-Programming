"""

# List: List is a collection which is ordered and changeable. Allows duplicate members.
# A list is a collection which is ordered and changeable. In Python lists are written with square brackets[].
"""

# Creating list
names = ["tannima", "onnima","nadia"]
print(names)

# another way with list constructor
fruits = list(("apple", "banana")) # note the double round-brackets
print(fruits)


# accessing list members
print(names[0])

# with negative index
print(names[-1]) # -1 = nadia, -2 = onnima, -3 = tannima

# Range of Indexes
print(names[1:3])  # Output 2nd and 3rd item
print(names[:2])   # Output: from beginning to 2nd item
print(names[2:])   # Output: from 3rd to last item

# Change item value
names[0]= "shishir"
print(names)

# loop through list
for name in names:
    print(name)

# check item is exits or not
if "shishir" in names:
    print("Yes, Shsihir is present")

# list legth
print(len(names))

# add item
names.append("tannima")
print(names)

# remove item: remove, del, pop
# pop: remove the last item
# del : remove with index
# remove: remove with item
names.pop()
print(names)

names.remove("nadia")
print(names)

del names[1]
print(names)

# Clear list
names.clear()
print(names)

# join two list: +, append, extend
list1 = ["1", "2"]
list2 = ["3", "4"]
list3 = list1 + list2
print(list3)
  # another way
for item in list2:
    list1.append(item)
print(list1)

  # with extend
list1 = ["1", "2"]
list2 = ["3", "4"]
list1.extend(list2)
print(list1)




