def fibo(a,b):
    while(True):
        yield a
        a,b=b,a+b

a = fibo(0,1)
for i in a:
    if(i>500):
        break
    print(i)
