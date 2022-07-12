file_name_write = "file_name_write.txt"

class TypeWriter():
    def __init__(self):
        '''No particular attributes needed'''

    def create_and_write(self,title):
        with open(file_name_write, "w") as write_object:
            write_object.write(title + "\n")

    def append_input(self, prompt):
        with open(file_name_write, "a") as update_object:
            update_object.write("-" + input(prompt) + "\n")

    def read_the_file(self):
        with open(file_name_write) as read_object:
            print(read_object.read())

'''
my_write_file = TypeWriter()

my_write_file.create_and_write()
my_write_file.read_the_file()
my_write_file.append_input()
my_write_file.read_the_file()
'''

notebook = TypeWriter()
notebook.create_and_write("Why people love programming?")
for times in range(5):
    notebook.append_input("Why do you love programming? ")
notebook.read_the_file()