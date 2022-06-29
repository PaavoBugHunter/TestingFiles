class Cars:
    '''Simple class to create cars'''
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 #Creates odometer attribute for the car and sets its default-value to zero(0)

    def vehicle_description(self):
        '''Returns consice description about the car'''
        car_name = f"{self.make} {self.model} {self.year}"
        return car_name.title()

    def read_odometer(self):
        '''Prints car's odometer reading'''
        print(f"{self.make} {self.model} has {self.odometer_reading} miles on it")

    def update_odometer(self, mileage):
        '''Adds mileage to car's odometer'''
        if mileage >= self.odometer_reading:
            self.odometer_reading += mileage
        else:
            print("You can't roll back on odometer")


class ElectricCar(Cars): #"Cars" in parenthesis indicates ElectricCar-class to be child-class of the Cars-class"
    '''Represents aspects of a car - electric car to be precise'''

    def __init__(self, make, model, year, battery):
        '''
        Initialize attributes of the parent class.
        Then initialize attributes of electric car.
        '''
        super().__init__(make, model, year) #The super()-function imports all attributes and methods from Cars-class to ElectricCars-class. Alternative expression here is Cars.__init__(self, make, model, year):
        self.battery = battery

    def describe_battery(self):
        print(f"This car, {self.make} {self.model}, has {self.battery}-kWh battery")

my_car = Cars("Porsche", "911", 2017)
print(my_car.vehicle_description())

my_tesla = ElectricCar("Tesla", "Model S", "2020", 80)
print(my_tesla.vehicle_description())
my_tesla.describe_battery()

'''Simple mileage addition and then reading'''
my_car.odometer_reading = 32
my_car.read_odometer()

'''Mileage-addition through a method'''
my_car.update_odometer(90)
my_car.read_odometer()

