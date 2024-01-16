class Parent:
    name = "Shashi"
    def __init__(self):
        print("in parent constructor")
        self.x = 10;

    def fun(self):
        print("in fun")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("in child constructor")
        super().fun()
        print(super().name)
        print(super().x)

obj = Child()
