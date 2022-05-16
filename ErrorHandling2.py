def myNewFunction(*args):
    print(sum(*args))
    return sum(*args)

def mySecondFunction(my_list):
    for element in my_list:
        print(element) #Only for test purposes

        try:#myNewFunction with every unit in the element
            myNewFunction(element)

        except Exception as exc:
            print(exc)

        finally:
            print("Here at last.")

mySecondFunction([(1,2),(1,2,3,),(1,"Moi")])