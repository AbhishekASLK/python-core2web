class Test:

    def m1(self):
        Test.x = 10

    y = 20

print(Test.__dict__)
Test().m1()
print(Test.__dict__)
