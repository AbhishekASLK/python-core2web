class Test:

    a = 10

    def __init__(self):
        self.x = 20

    @classmethod
    def m1(cls):
        print(cls.x)

Test.m1()
