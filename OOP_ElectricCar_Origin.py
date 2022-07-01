from OOP_Cars_Origin import Cars
from OOP_Battery_Origin import Battery

class ElectricCar(Cars): #"Cars" in parenthesis indicates ElectricCar-class to be child-class of the Cars-class"
    '''Represents aspects of a car - electric car to be precise'''

    def __init__(self, make, model, year):
        '''
        Initialize attributes of the parent class.
        Then initialize attributes of electric car.
        '''
        super().__init__(make, model, year) #The super()-function imports all attributes and methods from Cars-class to ElectricCars-class. Alternative expression here is Cars.__init__(self, make, model, year):
        self.battery = Battery() #Establishes an instance of Battery-class as an attribute of ElectricCar
