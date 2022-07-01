from random import randint

class Die:
    '''Die with a number of sides to be given upon instantiation'''
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        die_side = randint(1, self.sides)
        print(f"Rolled die-side is {die_side}")

my_die = Die(10)
my_other_die = Die(20)

for roll in range(0,10):
    my_die.roll_die()
    my_other_die.roll_die()