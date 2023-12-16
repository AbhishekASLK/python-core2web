class Test:

    def __init__(self):
        self.a = 10
        self.b = 20

    def m1(self):
        self.c = 30

t = Test()
print(t.c)
t.m1()
print(t.c)
