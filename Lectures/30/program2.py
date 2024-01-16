class Parent:
    def fun(self,x):
        print('in parent fun')

class Child:
    def fun(self):
        print('in child fun')

obj = Child()
obj.fun(10)
