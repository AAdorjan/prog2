"""
Write a Python class which has get_String two methods and print_String.
get_String accept a string from the user and print_String print the string in upper case.

"""
class Sztring:

    def __init__(self):
        self.s = "" #kezdetben üres a sztring

    def get_String(self):
        self.s = input("Adjon meg egy sztringet! ")

    def print_String(self):
        print(self.s.upper())


sztring1 = Sztring()
sztring1.get_String()
sztring1.print_String()