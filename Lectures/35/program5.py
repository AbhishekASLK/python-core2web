
from abc import ABC, abstractmethod

class Demo(ABC):
    @abstractmethod 
    def fun(self):
        print('in abstract fun')

class Memo(Demo):
    pass

Demo()
# Memo ne body nahi di phir bhi code chalega, wah object banane ke baad error dega
