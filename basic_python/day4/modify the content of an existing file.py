import os
file1= open("C:/Users/krish/OneDrive/Desktop/python/file_management.txt",'w')
l= ['Adding new data to an existing file. \n' ,'This is done in writing mode.\n']
file1.writelines(l)
file1.close()

file1= open("C:/Users/krish/OneDrive/Desktop/python/file_management.txt ",'r')
print(file1.read())
file1.close()

file1= open("C:/Users/krish/OneDrive/Desktop/python/file_management.txt",'a')
m= ['Appending new data to an existing file. \n' ,'This is done in appending mode.\n']
file1.writelines(m)
file1.write('This is the end of this file.')
file1.close()

file1= open("C:/Users/krish/OneDrive/Desktop/python/file_management.txt ",'r')
print(file1.read())
file1.close()

#os.remove("C:/Users/krish/OneDrive/Desktop/python/file_management.txt")

if os.path.exists("C:/Users/krish/OneDrive/Desktop/python/file_management.txt"):
   print("File exists")
 #  os.remove("C:/Users/krish/OneDrive/Desktop/python/file_management.txt")
else:
   print("File does not exist.")


