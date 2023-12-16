class Test:
    
    @classmethod
    def m1(cls):
        cls.x = 10
        print(cls.x)

t = Test()
t.m1()
print(t.__dict__)
