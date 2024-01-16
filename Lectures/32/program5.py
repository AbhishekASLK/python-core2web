class Demo:
    def __new__(self):
        print("object is created")
        return object.__new__(self)
    def fun(self):
        print("fun")

obj = Demo()
obj.fun()
