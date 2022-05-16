def myfunction(*args):
    print(args)
    for item in args:
        if len(item) <= 4:
            print(item + " Yupii!")
        else:
            print(item + " Yipii!")

def mykwargs_function(**kwargs):
    print(kwargs)
    for keyword, value in kwargs.items():
        print("Keyword: " + keyword)
        print("Value: " + value + "\n")

myfunction("pavvo", "cat", "Kvarkit", "Pah", "Ja pyh!", "Ui!")

#mykwargs_function(MyName="1", Pet="Hökötti", When_I_swear="Pah!")
