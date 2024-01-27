'''
class Demo:
    def __str__(self):
        print("Hello")

obj = Demo()
print(obj)

'''
# whenever we are trying to print the object reference then __str__ is called
class Demo:
    def __str__(self):
        return ("Hello")

obj = Demo()
print(obj)
