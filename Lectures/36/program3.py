
from abc import ABC,abstractmethod

class Parent(ABC):
    
    def __init__(self):
        print('Parent Constructor')
    
    @abstractmethod
    def marry(self):
        print(id(self))
        print('hello world!')

class Child(Parent):
    def marry(self):
        print(id(self))
        Child().marry()
        print('hi')

Child().marry()
