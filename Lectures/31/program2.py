class Parent:
    def __init__(self,num):
        self.__num = num

    def get_num(self):
        return self.__num

class Child(Parent):
    def __init__(self,num,val):
        super().__init__(num)
        self.__val = val

    def get_val(self):
        return self.__val

son = Child(100,200)
print(son.get_num())
print(son.get_val())
