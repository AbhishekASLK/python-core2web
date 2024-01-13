class Parent:
    def __init__(self):
        self.x = 10
    def fun(self):
        print(self.x)
    
class Child(Parent):
    pass

obj = Child()
obj.fun()

