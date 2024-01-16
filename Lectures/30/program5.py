class Parent1:
    def __init__(self,x):
        print("Parent1 constructor")

class Parent2:
    def __init__(self):
        print("Parent2 constructor")

class Child(Parent2,Parent1):
    pass

Child()
