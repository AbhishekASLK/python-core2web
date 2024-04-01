def gun():
    print("In gun")

def run(y):
    print("in run")
    y()

def fun(x):
    print("In fun")
    x()

fun(run(gun))
