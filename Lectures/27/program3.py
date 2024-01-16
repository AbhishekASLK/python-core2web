def fun():
    print("Start")
    yield 10
    yield 20
    yield 30
    print("End")

for i in fun():
    print(i)
