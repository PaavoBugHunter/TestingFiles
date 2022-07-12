class Calculator():
    '''Divides the two prompted integers'''
    def __init__(self):
        self.int2 = 0

    def prompt_and_divide(self):
        while self.int2 == 0:
            self.int1 = int(input("Give an integer"))
            self.int2 = int(input("Give another integer"))

            try:
                answer = (self.int1/self.int2)
            except:
                print("Something's gone wrong. Check your number\n")
                continue
            else:
                print(answer)

my_calculator = Calculator()

my_calculator.prompt_and_divide()

