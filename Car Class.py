class Car:
    def __init__(self, model, year,color, mileage=0):

        self.model = model
        self.year = year
        self.color=color
        self.mileage = mileage

    def display_info(self):
        print(f"Car Details: {self.model} {self.year} {self.color}")
        print(f"Mileage: {self.mileage} miles")

    def drive(self, miles):
        self.mileage += miles
        print(f"Driving {miles} miles. New mileage: {self.mileage} miles")

    def service(self):
        print(f"Servicing the {self.color} {self.model}... Mileage reset.")
        self.mileage = 0

my_car = Car("Fortuner" , 2025, "Black")
my_car.display_info()
my_car.drive(150)
my_car.display_info()
my_car.service()
my_car.display_info()