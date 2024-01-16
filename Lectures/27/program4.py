def fun():
    print("Start")
    yield 10
    yield 20
    yield 30
    print("End")

ret = fun()
print(next(ret))
print(next(ret))
print(next(ret))

try:
    next(ret)
except:
    pass
