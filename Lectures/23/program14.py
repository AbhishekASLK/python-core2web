class Test:

    def __init__(self):
        self.a = 10
        self.b = 20

    def m1(self):
        self.c = 30

t = Test()
print(t.__dict__)
t.m1()
print(t.__dict__)
