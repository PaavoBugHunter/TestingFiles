def myFunction(*args): #Solved, how to go through all myFunction calls and see their exception-descriptions
    print(sum(*args))
    return sum(*args)

my_list = [(1,2),(1,2,3,),(1,"Moi")]

def testFunction():

    for unit in my_list:
        try:
            myFunction(unit)

        except Exception as exc:
            print(exc)

        finally:
            print("End at last.")

testFunction()