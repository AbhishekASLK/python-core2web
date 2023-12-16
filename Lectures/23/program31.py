class Test:
    x = 30
    @classmethod
    def fun(cls):
        x = 10
        print(x)

t = Test()
t.fun()
