class Test:

    def __init__(self):
        self.a = 10
        self.b = 20
        self.c = 30
        self.d = 40

    def m1(self):
        del self.a

t = Test()
print(t.__dict__)
t.m1()
del t.d
print(t.__dict__)
