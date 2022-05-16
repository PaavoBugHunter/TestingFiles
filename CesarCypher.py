alphabetics = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def Cypher(my_string, converter):
    cyphered_word = []
    for letter in my_string:
        if letter in alphabetics:
            position = alphabetics.index(letter) + converter
            if position > 26:
                position = position - 26
            new_letter = alphabetics[position]
            cyphered_word.append(new_letter)
        else:
            cyphered_word.append(letter)
    cyphered_string = "".join(cyphered_word)
    return cyphered_string

'''print(cyphered_word)
    
    print(cyphered_string)'''


print(len(alphabetics))

secret_string = Cypher("Paavo v 12 o'clock", 2)

print(secret_string)
