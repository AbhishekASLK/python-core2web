def outer():
    print("start outer")
    def inner():
        print("inner")
    print("end outer")
    return inner()

f1 = outer()
f1()
