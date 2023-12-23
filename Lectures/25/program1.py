def gun():
    print('in gun')

def run(y):
    print('in run')
    y()

def fun(x):
    print('in fun')
    x()

fun(run(gun))
