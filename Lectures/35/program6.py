
from abc import ABC, abstractmethod

class Demo(ABC):
    @abstractmethod 
    def fun(self):
        print('in abstract fun')

class Memo(Demo):
    pass

Memo()
