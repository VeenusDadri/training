def fact(num):
    factorial=1
    for i in range(1,num+1):
        factorial*=i
    return factorial
number=int(input("Enter a no. to calculate factorial: "))
print(f"factorial of {number} is : {fact(number)}")
