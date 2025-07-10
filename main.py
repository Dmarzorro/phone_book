from book import *

class Menu:
    def __init__(self):
        self.contact_list = ContactList()

    def run(self):
        while True:
            self.show_menu()
            choice = input("Choose action: ")
            self.handle_choice(choice)

    def show_menu(self):
        print('\n===Welcome to Contact Book ===')
        print('1. Add Contact')
        print('2. Edit Contact')
        print('3. Delete Contact')
        print('4. Exit')

    choice = input("Choose action: ")


    def add_contact(self):
        first_name = input("First name: ")
        last_name = input("Last name: ")
        phone_number = input("Phone number: ")
        email = input("Email address: ") or None

        contact = Contact(first_name, last_name, phone_number, email)
        result = self.contact_list.add_contact(contact)
        print(result)

    def delete_contact(self):
        if not self.contact_list.contacts:
            print("No contacts to delete")
            return

        print("\n Choose contact to delete: ")
        for idx, contact in enumerate(self.contact_list.contacts, start=1):
            print(f"{idx}. {contact}")

        try:
            choice = int(input("Choose contact: "))
            contact = self.contact_list.contacts[choice]
            print(self)

