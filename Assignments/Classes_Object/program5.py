class ICC:
    def __init__(self):
        print("ICC Constructor")

    def rule1(self):
        print("rule1")

class BCCI(ICC):
    def __init__(self):
        print("BCCI Constructor")
    def rule2(self):
        print("rule2")

class IPL(BCCI):
    def __init__(self):
        print("IPL Constructor")

obj = IPL()
obj.rule1()
obj.rule2()
