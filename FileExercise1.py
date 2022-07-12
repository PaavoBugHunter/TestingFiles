file_variable = "PiDecimals.txt"
millpy = "PyMillionDecimals.txt"

class DecimalsOfPi:
    def __init__(self):
        '''How many decimals of pi come with it'''
        self.decimals = 10

    def pi_with_decimals(self):
        with open(file_variable) as object_representation:
            contents = object_representation.read()
        print(contents)

    def line_by_line(self):
        with open(file_variable) as my_object:
            for line in my_object:
                print(line)

    def lines_to_list(self):
        with open(file_variable) as lines_object:
            list = lines_object.readlines()

        pi_string = ""
        for line in list:
            pi_string += line.rstrip()

        print(pi_string)
        print(len(pi_string))

    def py_to_million(self):
        with open(millpy) as my_py_object:
            my_py_variable = my_py_object.read()
        #print(type(my_py_variable))
        print(my_py_variable[:self.decimals])
        print(len(my_py_variable))

    def birthday_in_py(self):
        birthday = input("\nType your birthday in ddmmyyyy: ")
        with open(millpy) as py_reference:
            my_py_string = py_reference.read()

        if birthday in my_py_string:
            print("Yipii! Your birthday's in first million decimals of py!")
        else:
            print("Naah. You're unlucky")



my_reading = DecimalsOfPi()

#my_reading.pi_with_decimals()

#my_reading.line_by_line()

#my_reading.lines_to_list()

my_reading.py_to_million()

my_reading.birthday_in_py()