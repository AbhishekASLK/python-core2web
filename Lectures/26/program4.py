def decorFun(func):
    def wrapper():
        print("Start Wrapper2")
        func()
        print("End Wrapper2")
    return wrapper

def decorRun(func):
    def wrapper():
        print("Start Wrapper1")
        func()
        print("End Wrapper1")
    return wrapper

@decorFun
@decorRun
def normalFun():
    print("In normal fun")
# normalFun = decorFun(decorRun(normalFun))
normalFun()
