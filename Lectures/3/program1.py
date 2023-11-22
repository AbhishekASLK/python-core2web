
# Type Casting

# 1. int()
'''
# float to int
a = 124.784
print(int(a))

# complex to int
a = 4+6j
#print(int(a)) # ERROR

# bool to int
a = False
print(int(a))

# string to int
a = "10"
b = "20"
a = int(a)
b = int(b)
print(a+b)

# float to int
a = "45.4"
#print(int(a)) # ERROR

a = "ten"
#print(int(a)) # ERROR

a = "0b111"
#print(int(a)) # ERROR

'''

# 2. float()

a = 10
print(float(a))

a = 10+5j
#print(float(a)) # ERROR

a = True
print(float(a))

a = False
print(float(a))

print(complex(False))

print(bool(""))
