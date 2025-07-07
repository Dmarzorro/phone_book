from book import *

class Menu:
    def __init__(self):
        self.contact_list = ContactList()

    def run(self):
        while True:
            self.show_menu(self)

    def show_menu(self):
        print('\n===Welcome to Contact Book ===')
        print('1. Add Contact')
        print('2. Edit Contact')
        print('3. Delete Contact')
        print('4. Exit')

    choice = input("Choose action: ")
