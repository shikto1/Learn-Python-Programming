class Person:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def printName(self):
        print(self.firstName, self.lastName)


p1 = Person("Shikto", "Shishir")
p1.printName()


# Inheritance
class Student(Person):
    pass


s1 = Student("Abu", "Osman")
s1.printName()


# Calling Super Class Constructor from Child Class Constructor
class Teacher(Person):
    def __init__(self, fName, lName):
        super().__init__(fName, lName)


t1 = Teacher("Abdul", "Sohel")
t1.printName()


# Calling Super Class Constructor from Child Class Constructor + Adding a extra parameter for Teache CLass
class Employee(Person):
    def __init__(self, fName, lName, age):
        super().__init__(fName, lName)
        self.age = age


t1 = Employee("Abdul", "Sohel", 36)
t1.printName()
print(t1.age)


"""
super() :

Python also has a super() function that will make the child class 
inherit all the methods and properties from its parent:

"""

"""
Multi level Inheritance
"""

class A:
    def display1(self):
        print("in side A")

class B(A):
    # display1() already inherited from class A
    def display2(self):
        print("in side B")

class C(B):
    # display1() by inheritance
    # display2() by inheritance
    def diplay3(self):
        print("in side C")

obj = C()
obj.display1()
obj.display2()
obj.diplay3()


"""
Multiple Inheritance
yes, though java is single inheritance, kotlin is also

python supports multiple inheritance
"""

class P:
    def display(self):
        print("in side P")

class Q:
    def display(self):
        print("in side Q")
class R(P, Q): # As P is prioritize so display method will be called from P
    pass

class S(Q, P):# But here Q is prioritize so display method will be called from Q
    pass

rObj = R()
rObj.display()

sObj = S()
sObj.display()
