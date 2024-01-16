
class Parent:
    x = 30

class Child(Parent):
    x = 10

obj = Child()
print(Child.x)


@staticmethod
def fun():
    print("A")

fun()
