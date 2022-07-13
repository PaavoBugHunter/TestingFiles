import json

class Memory_tool():
    '''Adds and retrieves data from menory'''
    def __init__(self, file_name):
        self.file_name = file_name

    def run_the_tool(self):
        try:
            with open(self.file_name) as file_object:
                user_name = json.load(file_object)

        except FileNotFoundError:
            user_name = input("What's your name? ")
            with open(self.file_name, "w") as file_object:
                json.dump(user_name, file_object)
                print(f"See you next time, {user_name}!")

        else:
            print(f"Welcome back {user_name}!")

my_memory_tool = Memory_tool("name_file.json")

my_memory_tool.run_the_tool()