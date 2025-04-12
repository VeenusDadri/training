# division program using if-else
num= float(input("Value of numerator is: "))
den= float(input("Value of denominator is: "))

if(den!=0):
    print("Division is :", num/den)
else:
    print("Denominator can't be Zero")


# division program using try...except block

try:
    num= float(input("Value of numerator is: "))
    den= float(input("Value of denominator is: "))
    print("Division is :", num/den)
except ZeroDivisionError:
    print("Denominator can't be Zero")

except ValueError:
    print("Input is invalid")


# division using a function
def numbers(num1,num2):
    try:
        result=num1/num2
        return result
    except ZeroDivisionError:
        return"cannot divide by zero!"
num1=float(input("Enter numerator:"))
num2=float(input("Enter denominator:")) 
print(numbers(num1,num2))