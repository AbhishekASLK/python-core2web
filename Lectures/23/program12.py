class Test:

    @classmethod
    def m1(self):
        print(id(self))

    @classmethod
    def m2(self):
        print(id(self))

print(id(Test))
Test.m1()
Test.m2()
