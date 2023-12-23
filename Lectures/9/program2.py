def first(num):
    n=1
    while n<=num:
        yield n
        n=n+1

values = first(5)
for i in values:
    print(i)
