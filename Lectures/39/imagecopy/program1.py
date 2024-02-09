# Created the pointer for loki.jpg file
f = open('loki.jpg','rb')

# Reading the content in binary
content = f.read()

# Opened the file copy.jpg in write mode to write the content of loki.jpg 
# which is in binary format
fcopy = open('copy.jpg','wb')

# Writing the binary content to copy.jpg with the help of fcopy pointer
fcopy.write(content)