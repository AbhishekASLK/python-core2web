class Test:

    @classmethod
    def m1(self):
        print('in m1')
        print('id of self or cls',id(self))

t = Test()
t.m1()
print('id of object t',id(t))
print('id of class: ',id(Test))
