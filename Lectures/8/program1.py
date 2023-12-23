def outer():
    print("outer fun")
    def inner():
        print("inner fun")
    return inner()
f = outer()
f()
