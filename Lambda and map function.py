#Use Lambda and map() to Add 2 to Each Number

numbers=[4,5,6,7,8,9]
def add2(num):
    return num+2

print("After adding 2 to each no.:")
print(list(map(add2,numbers)))


#Another way
numbers1=[1.1,2.2,3.3,4.4,5.5,6.6]
print("After adding 2 to each no.:")
print(list(map(lambda num: num+2 , numbers1)))





















