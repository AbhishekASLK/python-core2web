f1 = open('core2web.txt','a+')
friends = ['Ashish','Rahul','Badhe']
f1.writelines(friends)
f1.seek(0)
print(f1.read(34567))