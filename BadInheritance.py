#The idea with inheritance is to create classes based on previously created classes

#Study https://www.w3schools.com/python/trypython.asp?filename=demo_inheritance_add_method

class Animal():

    default_name = "No name"

    def __init__(self, name=default_name):
        self.name = name

    def who_am_I(self):
        print("I have {}".format(self.name))


class Dog(Animal): #=> Child class inherits parent's all properties and methods

    def __init__(self, name): #The __init__ -function here overrides the parent's init-function,
        super().__init__(name) #unless we import parent's all properties and functions
        self.name = name

    def who_am_I(self):
        print("My name is {}".format(self.name))

    def what_am_I(self):
        print("I am a dog")


my_animal = Animal()
dog_mauri = Dog("Mauri")


print(my_animal.name)
my_animal.who_am_I()
print(dog_mauri.who_am_I())
dog_mauri.what_am_I()
