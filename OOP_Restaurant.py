class Restaurant:
    #Simple restaurant class
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.name} offers {self.cuisine_type} food")

    def open_restaurant(self):
        print(f"Welcome! We are open.")

    def set_number_served(self, number_of_clients):
        self.number_served = number_of_clients

    def increment_number_served(self, new_clients):
        if new_clients < 0:
            print("You can't roll back number of guests")
        elif new_clients == 0:
            print("No need to add zero guests")
        else:
            self.number_served += new_clients

restaurant = Restaurant("Noste", "Thai")

class User:
    '''Framework for restaurant visitor'''

    def __init__(self, first_name, last_name, e_mail, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.e_mail = e_mail
        self.phone_number = phone_number

    def describe_user(self):
        print(f"Visitor's name is {self.first_name} {self.last_name}\n"
              f"Contact details are {self.e_mail} and {self.phone_number}")

    def greet_user(self):
        print(f"Hello Mr/Mrs. {self.last_name},\n"
              f"we're delighted to have you as our guest tonight")

print(restaurant.name)
print(restaurant.cuisine_type)
print("\n")

restaurant.describe_restaurant()
restaurant.open_restaurant()

ruoho_restau = Restaurant("Ruoho", "Finnish")
ant_restau = Restaurant("Ant", "Swedish")
björk_restau = Restaurant("Björk", "hungarian")

ruoho_restau.describe_restaurant()
ruoho_restau.open_restaurant()
print(ruoho_restau.number_served)
ruoho_restau.number_served = 11
print(ruoho_restau.number_served)
ruoho_restau.set_number_served(13)
print(ruoho_restau.number_served)

ant_restau.describe_restaurant()
ant_restau.open_restaurant()
ant_restau.increment_number_served(-2)
ant_restau.increment_number_served(0)
ant_restau.increment_number_served(4)
print(ant_restau.number_served)

björk_restau.describe_restaurant()
björk_restau.open_restaurant()

'''
mauri_visitor = User("Mauri", "Wof", "dog@couch.com", "123-Hau-456")
tötterö_visitor = User("Juli", "Tötterö", "juli@lelu.fi", "987654")

mauri_visitor.describe_user()
mauri_visitor.greet_user()

tötterö_visitor.describe_user()
tötterö_visitor.greet_user()
'''