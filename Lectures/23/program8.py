class Test:
    
    def __init__(self):
        print('no-arg constructor')

    def __init__(self,x):
        print('one-arg constructor')

t = Test(10)
t = Test()
