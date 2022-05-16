NumList = [1,2,3,4]
NameList = ["Paavo","Jari","Ile"]

def square_up(num):
    return num**2

def check_even(item_to_filter):
    return item_to_filter%2 == 0

print(*tuple(map(square_up,NumList)))    #Iterates square_up over Numlist and inserts results to a tuple
print(*tuple(filter(check_even,NumList)))    #Filters elements that pass True through check_even function
print(*tuple(map(lambda name:name[0],NameList))) #Iterates flipping name-variable(str) backwards over NameList and adds them to a tuple