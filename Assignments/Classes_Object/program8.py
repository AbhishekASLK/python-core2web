class Demo:
    def __init__(self):
        print("In constructor")

    def __del__(self):
        print("In destructor")

def Fun():
    print("In fun")
    obj = Demo()
    print("End fun")
    return obj

retObj = Fun()
print("End Code")
