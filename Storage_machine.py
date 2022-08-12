import json


class Storage_machine():
    '''Sotes give user_names to a JSON-file'''
    def __init__(self):
        self.storage_file = "name_file.json"

    def ask_and_store_name(self):
        user_name = input("Give your user name")
        with open(self.storage_file, "a") as file_object:
            json.dump(user_name, file_object)

my_machine = Storage_machine()
my_machine.ask_and_store_name()