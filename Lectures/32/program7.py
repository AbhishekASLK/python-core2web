class MyMetaClass(type):
    def __new__(cls,name,bases,dct):
        print("In MyMetaClass __new__")
        return super().__new__(cls,name,bases,dct)

class Demo(metaclass=MyMetaClass):
    pass

obj = Demo()
print(Demo)
