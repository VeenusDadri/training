# Score result
marks= int(input('Enter the marks out of 100 : '))
if marks>=90 :
    print( "Excellent")

elif marks>=80 :
    print("Above avg")

elif marks>=70 :
    print("Avg")

elif marks>=60 :
    print("Upto mark")

elif marks>=50 :
    print("Poor")

else :
    print ("Fail")

# Check if a year is a leap year or not
year=int(input("Enter a year : "))
if (year%4==0 and year%100!=0) or (year%400==0):
        print(f"{year} is a leap year")
else:
        print(f"{year} is not leap year")