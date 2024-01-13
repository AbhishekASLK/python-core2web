class Demo:
    def __del__(self):
        print("Destructor")

obj1 = Demo()
obj2 = Demo()
obj3 = Demo()
obj4 = Demo()

obj3 = obj1
del obj2
