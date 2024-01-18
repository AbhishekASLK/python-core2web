from abc import ABC,abstractmethod
class Demo(ABC):
    
    def fun(self):
        print('in abstract fun')

obj = Demo()
obj.fun()
