class Person():
    def __init__(self, fname, lname): #Parent class's attributes or characteristics: first and last name
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname) #Parent class's function or action: printing first and last name

x = Person("John", "Doe")
x.printname()

class Student(Person):
    def __init__(self, fname, lname, gyear): #Child's init-method overrides the init-method from the Person-parent class
        Person.__init__(self, fname, lname) #Calling Person's init-method here keeps its attributes and functions in the Student-class. Super-method is alternative.
        self.graduationyear = gyear         #Graduationyear-attribute is added to the student-class

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "of year", self.graduationyear)

y = Student("Michael", "Moore", 2012)
y.printname()
y.welcome()