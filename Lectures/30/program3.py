class A:
    def fun(self,x):
        print("A")

class B:
    def fun(self):
        print("B")

class C(A,B):
    pass

C().fun()
