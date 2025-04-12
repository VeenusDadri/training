num1=float(input("Enter 1st number:"))
num2=float(input("Enter 2nd number:")) 

def add(num1,num2):
    try:
        print("Addition of 2 no. is: ",num1+num2)
    except:
        print("You have not entered a valid no.")
    finally:
        print("Operation is complete")

add( num1,num2)
        
