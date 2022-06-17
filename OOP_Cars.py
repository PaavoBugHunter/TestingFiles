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

my_car = Cars("Porsche", "911", 2017)
print(my_car.vehicle_description())

'''Simple mileage addition and then reading'''
my_car.odometer_reading = 32
my_car.read_odometer()

'''Mileage-addition through a method'''
my_car.update_odometer(90)
my_car.read_odometer()