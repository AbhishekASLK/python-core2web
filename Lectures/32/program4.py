def new(cls):
    print("Object is created")
    return object.__new__(cls)

Demo = type("Demo",(),{"__new__":new})

obj = Demo()
