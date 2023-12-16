class Test:
    a = 10

    def __init__(self):
        Test.b = 20

print(Test.__dict__)
Test()
print(Test.__dict__)

