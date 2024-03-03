obj = open('core2web.txt','rb')
obj.seek(-11,2)

print(obj.read().decode('UTF-8'))
obj.seek(-11,1)

print(obj.read().decode('utf-8'))