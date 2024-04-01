def table():
    n = 2
    while(True):
        yield n
        n = n + 2;

t = table()

for i in t:
    print(i)
