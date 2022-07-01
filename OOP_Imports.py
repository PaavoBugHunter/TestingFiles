from OOP_Cars_Module import Cars, ElectricCar #Write only attributes and methods to a class. Don't make instances with them.

audi = Cars("Audi", "R8", 2021)
print(audi.vehicle_description())
audi.read_odometer()

print("\n")

polestar = ElectricCar("Polestar", "Northstar", 2022)
print(polestar.vehicle_description())
polestar.battery.describe_battery()
polestar.battery.upgrade_battery(12)
polestar.battery.estimate_range()