class Parent:
    def __init__(self):
        print('hi')

class Demo(Parent):
    def __init__(self):
        print(super())

Demo()
