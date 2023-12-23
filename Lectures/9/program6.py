class Alphabet():
    def __init__(self):
        print("Parent Constructor")
    def fun(self):
        print("in fun of parent")

class Google(Alphabet):
    pass


Alphabet()
