from OOP_Cars_Origin import Cars
from OOP_ElectricCar_Origin import ElectricCar

dodge_viper = Cars("Dodge", "Viper", 2018)
porsche_taycan = ElectricCar("Porsche", "Taycan", 2021)

print(dodge_viper.vehicle_description())
dodge_viper.read_odometer()

print("\n")

print(porsche_taycan.vehicle_description())
porsche_taycan.read_odometer()
porsche_taycan.battery.describe_battery()
porsche_taycan.battery.estimate_range()