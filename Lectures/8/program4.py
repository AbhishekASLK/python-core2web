class Test:

    @classmethod
    def m1(this):
        this.x = 10
        print(this.x)

t = Test()
t.m1()
print(t.__dict__)
