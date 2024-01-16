class Child:
    def m1(self):
        val = self.m1() + 20
        return val

obj = Child()
obj.m1()
