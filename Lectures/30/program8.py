class Parent:
    def __init__(self):
        print(id(self))
        print("Parent Constructor")

class Child(Parent):
    def __init__(self):
        print(id(self))
        super.__init__(super())
        print("Child Constructor")

Child()
