class Battery():
    '''Simple class to describe a 65-kWh-battery and its behaviors'''
    def __init__(self):
        self.battery_reserve = 65

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
