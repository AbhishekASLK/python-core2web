class Test:
    x = 30
    
    def __init__(self):
        self.y = 40

    @classmethod
    def fun(cls):
        x = 10
        print(x)
        print(cls.y)

t = Test()
t.fun()
