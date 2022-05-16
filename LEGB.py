name = "Paavo"

def print_name():
    name = "Jarppa"
    print(name)

    def anothername():
        name = "Ville"
        print(name)
    anothername()


print_name()
print("Original name: "+name)

'''
Jarppa
Ville
Original name: Paavo

'''