class Calculator():
    '''Divides the two prompted integers'''
    def __init__(self, books):
        self.int2 = 0
        self.books = books

    def prompt_and_divide(self):
        while self.int2 == 0:
            self.int1 = int(input("Give an integer"))
            self.int2 = int(input("Give another integer"))

            try:
                answer = (self.int1+self.int2)
            except ZeroDivisionError:
                print("The denominator is zero. Check the number\n")
                continue
            except ValueError:
                print("Something went wrong. Hmm... check that both inputs were numbers")
                continue
            else:
                print(answer)
                print("\nWell done!")

    def count_words(self):
        for book in self.books:
            try:
                with open(book) as text_object:
                    content = text_object.read()
                    list_of_words = content.split()

            except FileNotFoundError:
                print("File wasn't found")

            else:
                count_of_words = len(list_of_words)
                print(f"The number of words in {book} is {count_of_words}")


my_calculator = Calculator(['file_name_write.txt', "Absent_book.txt", "PiDecimals.txt", "PyMillionDecimals.txt"])

my_calculator.prompt_and_divide()
my_calculator.count_words()

