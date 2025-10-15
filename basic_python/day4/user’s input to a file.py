import os
file1= open("C:/Users/krish/OneDrive/Desktop/python/file_management1.txt",'w')
l= ['Trying to create a new file.\n' ,'This is done in writing mode.\n']
file1.writelines(l)
file1.close()

file1= open("C:/Users/krish/OneDrive/Desktop/python/file_management1.txt ",'r')
print(file1.read())
file1.close()
