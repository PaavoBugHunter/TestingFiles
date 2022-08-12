import json

class Memory_tool():
    '''Adds and retrieves data from menory'''
    def __init__(self, file_name):
        self.file_name = file_name

    def search_user_name(self):
        '''Searches for existing JSON-file and user name'''
        try:
            with open(self.file_name) as file_object:
                user_name = json.load(file_object)

        except FileNotFoundError:
            return None

        else:
            return user_name

    def prompt_and_save_user_name(self):
        '''Asks user to input her/his user name and stores it JSON-file'''

        prompted_name = input("Type a user name")
        with open(self.file_name, "w") as file_object:
            json.dump(prompted_name, file_object)

        return prompted_name

    def greet_user(self):
        '''Greets user according to her/his respective situation'''
        user = self.search_user_name()
        if user:
            print(f"Welcome back {user}!")
        else:
            user = self.prompt_and_save_user_name()
            print(f"We'll see you next time, {user}")

my_other_tool = Memory_tool("name_file.json")
my_other_tool.greet_user()