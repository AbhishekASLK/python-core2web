class Test:
    a = 10
    def m1(self):
        self.a = 888

t1 = Test()
t1.m1()
print(Test.a)
print(t1.a)
