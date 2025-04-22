# sum of numbers

sum=0
x=10
for i in range(0,x):
    sum+=i
print(f"Sum of numbers is : {sum}")

# calculate factorial

num = int(input("Enter a no. to calculate factorial of that no.: "))
factorial=1
i=1
while i <= num:
    factorial*=i
    i+=1
print (f"factorial of {num} is : {factorial}")

# draw pattern
rows = int(input("Enter the no. of rows: "))
col = int(input("Enter the no. of columns: "))
for i in range(0, rows):
    print("*" * col)
    