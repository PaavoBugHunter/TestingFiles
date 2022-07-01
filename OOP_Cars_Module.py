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


class Battery():
    '''Simple class to describe a battery and its behaviors'''
    def __init__(self):
        self.battery_reserve = 75 #No need parameterize battery_reserve in the init-function since every battery-instance has default-charge of 75kWh

    def describe_battery(self):
        '''Print how much reserve the battery has'''
        print(f"This car has {self.battery_reserve}-kWh battery")

    def estimate_range(self):
        '''Gives estimate about drive-range with the battery-reserve'''
        if self.battery_reserve >= 70 and self.battery_reserve <= 75:
            range = 100
        elif self.battery_reserve < 70:
            range = 90
        else:
            range = 110

        print(f"Estimated drive-distance with this battery is {range}Km.")

    def upgrade_battery(self, upload):
        '''Increase battery-charge by upload-amount'''
        self.battery_reserve += upload
        print(f"Battery uploaded with {upload}-Kwh")


class ElectricCar(Cars): #"Cars" in parenthesis indicates ElectricCar-class to be child-class of the Cars-class"
    '''Represents aspects of a car - electric car to be precise'''

    def __init__(self, make, model, year):
        '''
        Initialize attributes of the parent class.
        Then initialize attributes of electric car.
        '''
        super().__init__(make, model, year) #The super()-function imports all attributes and methods from Cars-class to ElectricCars-class. Alternative expression here is Cars.__init__(self, make, model, year):
        self.battery = Battery() #Establishes an instance of Battery-class as an attribute of ElectricCar
