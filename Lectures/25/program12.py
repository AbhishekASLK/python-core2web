def decor1(fun):
    def inner(name):
        print("First Decor")
        fun(name)
    return inner

def decor2(fun):
    def inner(name):
        print("Second Decor")
        fun(name)
    return inner

@decor1
@decor2
def wish(name):
    print("Hello",name)

wish("Shashi")
