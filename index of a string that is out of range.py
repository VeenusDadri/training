string=str(input("Enter the string:"))
index=int(input("Enter the index:"))

try:
    print("Character at index", index, "of string", string, 'is', string[index])
except:
    print("Index out of range")


my_list=[10,20,30,40,50]  
print("Checking for a list")  
try:
    print(my_list[10])
except IndexError:
    print("Error:index is out of range!")