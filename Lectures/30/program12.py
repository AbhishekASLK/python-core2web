class object:
    def __init__(self):
        print('Parent')

class object(object):
    def __init__(self):
        super().__init__()
        print('Child')

obj = object()
