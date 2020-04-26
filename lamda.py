# Lamda
"""
0. def change to lamda keyword
1. Name will be remove. Because lamda is actually anonymous function or nameless function
2. remove return keyword
"""


# Example :01
def square(a):
    return a * a


print(square(5))

l = lambda a: a * a
result = l(5)
print(result)


#  Example : 02

def add(a, b):
    return a + b


print(add(5, 5))

# Making lamda expression
f = lambda a, b: a + b
result = f(5, 5)
print(result)

# Example : 03
full_name = lambda fName, lName: f"{fName.strip()} {lName.strip()}"
print(full_name("Shikto        ", "     Shishir"))

'''
** Lamda or nameless function is not as powerful as named function
** Lamda can work with only single expression/ single line of code.

'''
