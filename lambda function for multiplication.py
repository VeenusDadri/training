#lambda function for multiplication

num1= float(input("Enter 1st number:"))
num2= float(input("Enter 2nd number:"))
multiply= lambda a,b: print("Mutiplication is:", num1*num2 )
multiply(num1,num2)


Multiply=lambda x,y:x*y
print(Multiply(5,6))

#example1
products=[
    {"name":"laptop","price":900},
    {"name":"smartphone","price":500},
    {"name":"Tablet","price":300},

]
sorted_products=sorted(products,key=lambda x:x['price'])
print(sorted_products)

#Example2
fruits =["apple","banana","kiwi","orange","pear"]
filtered_fruits = list(filter(lambda x:len(x)>5,fruits))
print(filtered_fruits)

#example3
vegetables=[("carrot",2.5),("Tomato",3.5),("cucumber",2.0),("potato",4.0)]
expensive_vegetables =list(filter(lambda x:x[1]>3,vegetables))
print(f"vegetables with price greater than 3:{expensive_vegetables}")

#example4
from datetime import datetime
products = [
    {"name":"Milk","expiry":"2025-01-05"}
    {"name":"cheese","expiry":"2025-02-2"}
    {"name":"butter","expiry":"2025-01-25"}
]
today=datetime.now().strftime('%y-%m-%d')
expired_products =list(filter(lambda x:x['expiry']<today,products))
print(expired_products)