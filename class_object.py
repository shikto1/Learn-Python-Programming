class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"{self.name} is {self.age} years old.")


p1 = Person("Shishir", 27)
p1.display()

'''
 The self parameter is a reference to the current instance of the class, 
 and is used to access variables that belongs to the class.

 It does not have to be named self , you can call it whatever you like,
 but it has to be the first parameter of any function in the class:
'''


class Student:
    def __init__(myObj, name):
        myObj.name = name

    def showName(obj):
        print(f"My name is {obj.name}")

s1 = Student("Shishir")
s1.showName()


