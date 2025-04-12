# scope of variable
 
a = 1
   
# Uses global because there is no local 'a' 
def f(): 
    print('Inside f() : ', a)
   
# Variable 'a' is redefined as a local 
def g():     
    a = 2
    print('Inside g() : ', a)
   
# Uses global keyword to modify global 'a' 
def h():     
    global a 
    a = 3
    print('Inside h() : ', a) 
   
# Global scope 
print('global : ', a)
f() 
print('global : ', a) 
g() 
print('global : ', a)
h() 
print('global : ', a) 


# nonlocal keyword
 
print("Value of a using nonlocal is : ", end="")
 
 
def outer():
    a = 5
 
    def inner():
        nonlocal a
        a = 10
    inner()
    print(a)
 
 
outer()
 
# demonstrating without non local
# inner loop not changing the value of outer a
# prints 5
print("Value of a without using nonlocal is : ", end="")
 
 
def outer():
    a = 5
 
    def inner():
        a = 10
    inner()
    print(a)
 
 
outer()