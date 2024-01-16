class Demo:
    def __init__(self):
        print('Parent Demo')
        print(id(Demo))

class Demo(Demo):
    def __init__(self):
        super().__init__()
        print('Child Demo')
        print(id(Demo))

obj = Demo()

print(id(Demo))
