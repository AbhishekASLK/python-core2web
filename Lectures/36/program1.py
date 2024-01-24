
class Parent:
    def __init__(self):
        print('parent constructor')
    
    def marry(self):
        print('marry')

obj = Parent()
Parent.marry(obj)
