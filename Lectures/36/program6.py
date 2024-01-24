
class Abhishek(type):
    pass

class Demo():
    pass

class Demo(Demo, metaclass=Abhishek):
    pass

print(type(Demo))

