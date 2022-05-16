#Idea is that one function takes another as its argument and returns a third function as the outcome

def deco_function(to_be_decoed):

    def what_deco_does():
        empty_list = []
        print("Something before to_be_decoed")
        empty_list.append(1)

        to_be_decoed()

        print("Something after to_be_decoed")
        return empty_list

    return what_deco_does


@deco_function
def core_function():
    print("I'm the core-function")

core_function()