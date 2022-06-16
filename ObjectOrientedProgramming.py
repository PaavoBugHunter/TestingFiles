class Dog:
    #A simple dog-class with name and age attributes, and sit and rol-over actions
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is now sitting")

    def roll_over(self):
        print(f"{self.name} just rolled over!")


my_dog = Dog("Mauri", 3)
your_dog = Dog("Huffy", 4)

print(f"Wof, my name is {my_dog.name} and I'm {my_dog.age} years old!")
print(f"Meow, my name is {your_dog.name} and I'm {your_dog.age} years old!\n")

my_dog.sit()
my_dog.roll_over()

print("\n")

your_dog.sit()
your_dog.roll_over()