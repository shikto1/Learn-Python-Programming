# Number Array
print("")
print("Number array>>>>")
numbers = [12, 34, 55, 88, 33]
for number in numbers:
    print(number)


# Fruits Array
print("")
print("Fruits array >>>>")
for fruit in ["Apple", "Mango", "Banana", "Cherry"]:
    print(fruit)


# Looping through String
print("")
print("Looping through String >>>>")
for c in "banana":
    print(c)


# break statement
print("")
print("Break Statement >>>>")
for number in [1, 2, 3, 4]:
    if number == 3:
        break
    print(number)


# Continue Statement
'''
 Continue is used to skip rest of the statement. Continue means:
 No need to execute rest of the statement, go back to loop.
'''
print("")
print("Continue Statement >>>>")
for number in [1, 2, 3, 4, 5]:
    if number == 2:
        continue
    print(number)


# Pass Statement
'''
'''
print("")
print("Pass Statement >>>>")
for number in [1, 2, 3, 4]:
    if number == 2:
        pass
    else:
        print(number)
