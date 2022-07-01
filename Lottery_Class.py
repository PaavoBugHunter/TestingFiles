from random import randint
from string import ascii_lowercase

class Deck:
    '''Deck of integers and lower-case alphabets to draw a lottery-hand'''
    def __init__(self, integer_population, drawn_integers):
        self.integer_population = integer_population
        self.drawn_integers = drawn_integers
        self.list_of_integers = []
        self.list_of_letters = []
        self.draw = []

        for i in range(0,self.integer_population):
            self.list_of_integers.append(i)

        for letter in ascii_lowercase:
            self.list_of_letters.append(letter)

    def show_list(self):
        print(self.list_of_integers)
        print(self.list_of_letters)

    def draw_a_hand(self):
        for i in range(0,self.drawn_integers):
            integer_list_index = randint(0,len(self.list_of_integers)-1)
            self.draw.append(self.list_of_integers[integer_list_index])
            self.list_of_integers.pop(integer_list_index)

        for i in range(1):
            alphabet_list_index = randint(0, len(self.list_of_letters)-1)
            self.draw.append(self.list_of_letters[alphabet_list_index])
            self.list_of_letters.pop(alphabet_list_index)

        print(self.draw)


