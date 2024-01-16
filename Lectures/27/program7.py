def fun():
    print("Start")
    yield 10
    yield 20
    yield 30
    print("End")
    yield 

ret = fun()
print(next(ret))
print(next(ret))
print(next(ret))
if next(ret)==None:
    pass
