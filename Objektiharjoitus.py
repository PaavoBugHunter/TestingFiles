class Bike():   #Bike-object defined here
    def __init__(self, brand, genre):   #Attributes of every instance of Bike-object are given here and tied to Bike-class
        self.brand = brand
        self.genre = genre

my_bicycle = Bike(brand="Trek", genre="Fatbike")    #Parameters of brand and genre are given here and assigned to self.(my)brand and self.(my)genre attributes.

print("My bike is " + my_bicycle.brand + " " + my_bicycle.genre)    #Executes print-method with (self.)brand's and (self.)genre's parameters
