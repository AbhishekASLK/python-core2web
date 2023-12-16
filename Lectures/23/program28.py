class Test:

    a = 777

    @classmethod
    def m1(cls):
        cls.a = 888

    @staticmethod
    def m2():
        Test.a = 999
        print(type(staticmethod))
print(Test.a)
Test.m1()
print(Test.a)
Test.m2()
print(Test.a)
