class Parent:
    #instance
    def fun(self):
        print("Parent instance")

    @staticmethod
    def gun():
        print("Parent static")

    @classmethod
    def tun(cls):
        print("Parent class method")

class Child(Parent):
    pass

obj = Child()
obj.fun()
obj.tun()
obj.gun()
