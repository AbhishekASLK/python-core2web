def normal(**args):
    sum=0
    for k,v in args.items():
        sum+=v
    return sum

print(normal(x=10,y=20))
