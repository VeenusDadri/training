# lambda function that returns "Yes" if a number is greater than 10, and "No" otherwise

num= float(input("Enter a no.:"))
check_greater_than_10=lambda n: print("Yes, This no. is greater than 10") if n>10  else print("Entered no. is not greater than 10")
check_greater_than_10(num)


# Another way
num1= float(input("Enter another no. to check:"))
check=lambda n: "Yes" if n>10  else "No"
result= check(num1)
print("Is ",num1 ,"greater than 10:",result)