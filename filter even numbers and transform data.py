# filter even number

num=[1,2,3,4,5,6,7,8,9,10]
print("even numbers are:")
for i in num:
    if i%2==0:
        print(i) 
odd_num= [j for j in num if j%2!=0]
print("odd numbers: ", odd_num)

##Transfrom data (square of numbers)
print("square of numbers is: ", [i**2 for i in range(1,5)])

# transform string to uppercase

words=['veenus','ritu','himanshu','krishna']
print("uppercase words are:", [word.upper() for word in words ])