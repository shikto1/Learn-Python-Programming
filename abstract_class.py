from abc import ABC, abstractmethod


class Person(ABC):

    @abstractmethod
    def showName(self):
        pass


class Student(Person):
    def showName(self):
        print("I am here")


s1 = Student()
s1.showName()


"""
  * Not possible to create object of abstract class
  * Abstract method must be implemented in child class
"""