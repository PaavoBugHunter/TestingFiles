#Idea is that one function takes another as its argument and returns a third function as the outcome

def deco_function(to_be_decoed):

    def what_deco_does():

        print("Something before to_be_decoed")

        to_be_decoed()

        print("Something after to_be_decoed")

    return what_deco_does


@deco_function
def core_function():
    print("I'm the core-function")

core_function()