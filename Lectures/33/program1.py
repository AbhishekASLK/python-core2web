class Abhishek(type):
    pass

class Baap():
    pass

class Beta(Baap, metaclass=Abhishek):
    pass

print(type(Beta))

