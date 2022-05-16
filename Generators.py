#Generators are functions that return a value, and pick from there with a subsequent call and returned value

import random
############## Exercise 1 ##############
def gensquare(n):
    for number in range(n):
        yield number**2

for i in gensquare(5):
    print(i)
############## Exercise 2 ##############
print("\n")

def genrandom(low, high):
    n_ex2 = random.randint(1, high)
    print("n_x2's initial value is: " + str(n_ex2))
    while n_ex2 > 0:
        yield random.randint(low, high)
        n_ex2 = n_ex2 - 1

for i in genrandom(1,5):
    print(i)