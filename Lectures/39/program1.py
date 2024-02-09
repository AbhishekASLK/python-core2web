# Opened the file in write and read mode
f = open('core2web.txt','w+')

# Writing the content
print(f.tell())
f.write('A')
print(f.tell())
f.write('B')
print(f.tell())

# Write karte karte wah file ke last main aa gya, to wah read kuch nahi
# kar payega
f.seek(0)

# Reading the content of core2web.text to content
content = f.read()

# Printing the content
print(content)

# Why it does not printing the "Abhishek"
# Because the pointer is at EOF