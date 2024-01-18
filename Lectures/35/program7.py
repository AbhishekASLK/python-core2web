from abc import ABC,abstractmethod

class Demo(ABC):
    def __init__(self):
        print('in constructor')

Demo()

# yeh bhi chalega, kyunki iske under koi abstract method nahi hai, agar hoti to can't instantiate the object ka error aata
