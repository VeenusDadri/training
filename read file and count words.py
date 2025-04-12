import os
file1= open("C:/Users/krish/OneDrive/Desktop/python/file_management.txt",'r')
# read the complete file
print(file1.read())

#bring the cursor to the nth char
file1.seek(0)

# read only 1st line
print(file1.readline())
file1.seek(0)

# read all the lines
print(file1.readlines())
file1.seek(0)

# read n char of the file
print(file1.read(40))
file1.seek(0)

# read n char of the file, but doen not exceed the first line
print(file1.readline(40))
file1.close()





