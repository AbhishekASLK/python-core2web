class Parent1:
    def __init__(self):
        print("Parent1 constructor")

class Parent2:
    def __init__(self):
        print("Parent2 constructor")

class Child(Parent1,Parent2):
    pass

Child()
