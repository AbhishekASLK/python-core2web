class Demo:
    def __init__(self,pages):
        self.pages = pages

    def __add__(self,other):
        print(id(self))
        print(id(other))
        return self.pages + other.pages

obj1 = Demo(100)
obj2 = Demo(200)
print(id(obj1))
print(id(obj2))
print(obj1+obj2)
