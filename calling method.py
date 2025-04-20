from abc import ABC,abstractmethod

#1.class & objects
class Person:
    def __init__(self,name,age):
        self.name=name #public attribute
        self.__age=age#private attribute(encapsulation)

    def display(self):
        print(f"name:{self.name},Age:{self.__age}")

    def get_age(self):  #getter for private attribute
        return self.__age
p1 = Person("Alice", 25)
p1.display()


#Inheritance
class Employee(Person):
    def __init__(self,name,age,salary):
        super().__init__(name,age)#calling parent constructor
        self.salary=salary

   #Method overriding
    def display(self):
        print(f"employee Name:{self.name},Age:{self.get_age()},Salary:{self.salary}")

emp1 = Employee("Bob", 30, 50000)
emp1.display()


#4.abstractions(using abc module)
class Shape(ABC):

 @abstractmethod

 def area(self):
    pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return 3.14*self.radius*self.radius

c = Circle(5)
print(f"Circle Area: {c.area()}")
    
# 5.polymorphism   
class MathOperations:
    def add(self,a,b,c=0):

        return a+b+c

math = MathOperations()
print(f"Addition (2 params): {math.add(5, 10)}")
print(f"Addition (3 params): {math.add(5, 10, 15)}")

 #6.static method
class Utils:
    @staticmethod
    def greet():
        print("welcome to oops")

Utils.greet()

#class method
class Company:
    company_name="Tech crop"
    @classmethod
    def set_company_name(cls,new_name):
        cls.company_name=new_name

print(f"Old Company Name: {Company.company_name}")
Company.set_company_name("NewTech Corp")
print(f"Updated Company Name: {Company.company_name}")       


        





