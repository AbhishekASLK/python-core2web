
from abc import ABC,abstractmethod

class Demo():
    @abstractmethod 
    def fun(self):
        print('in abstract fun')

print(dir(fun()))
#obj = Demo()
#obj.fun()
