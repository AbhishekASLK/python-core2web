class Parent:
    @staticmethod
    def fun():
        print("In Static Method")

class Child(Parent):
    pass

obj = Child()
obj.fun()
