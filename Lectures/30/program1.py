class Parent:
    def fun(self):
        print('in parent fun')

class Child:
    def fun(self):
        print('in child fun')

obj = Child()
obj.fun()
