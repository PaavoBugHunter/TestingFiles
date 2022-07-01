from Lottery_Class import Deck

population = int(input("Give range of numbers to lottery:"))
draws = int(input("Give number of draws to lottery:"))

while draws > population:
    print("\n")
    print(f"Given draws {draws} are more than population {population}. Please fix")
    population = int(input("Give range of numbers to lottery:"))
    draws = int(input("Give number of draws to lottery:"))

hand = Deck(population, draws)
hand.draw_a_hand()