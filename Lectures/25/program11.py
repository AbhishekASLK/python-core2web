def decor():
    print("extra functionality")
    fun()

def fun():
    print("low functionality")

fun = decor;
fun()
