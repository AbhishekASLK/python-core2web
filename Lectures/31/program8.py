class type():
    def __init__(self,b):
        print("Hello")

class Demo:
    pass

obj = Demo()
print(__builtins__.type(obj))
