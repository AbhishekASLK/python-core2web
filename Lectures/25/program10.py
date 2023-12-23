def decor(fun):
    def gun(name):
        print('gun')
    def inner(name):
        if(name == 'Shashi'):
            print('Teacher');
        else:
            gun(name)
    return inner

@decor
def fun(name):
    print('Student')

fun('Shashi')
