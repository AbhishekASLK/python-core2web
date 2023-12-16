class Test:
    x = 10
    def __init__(self):
        self.y = 20

t1 = Test()
t2 = Test()
print(Test.__dict__)
print(t2.__dict__)

print(t1.x,t1.y)
print(t2.x,t2.y)

Test.x = 888
t2.y = 999

print(t1.x,t1.y)
print(t2.x,t2.y)
