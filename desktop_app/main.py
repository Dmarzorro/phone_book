from desktop_app.book import *
from helper import *

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
        print('4. Show Contact list')
        print('5. Exit')

    def show_contacts(self):
        print(self.contact_list.show_contacts())

    def add_contact(self):
        first_name = prompt_valid("First name: ", validate_name)
        try:
            first_name = validate_name(first_name)
        except ValidationError as exc:
            print(f"Invalid first name {exc}")

        last_name = prompt_valid("Last name: ", validate_name)
        try:
            last_name = validate_name(last_name)
        except ValidationError as exc:
            print(f"Invalid last name {exc})")

        phone_number = prompt_valid("Phone number: ", validate_phone)
        try:
            phone_number = validate_phone(phone_number)
        except ValidationError as exc:
            print(f"Invalid phone number {exc}")

        email = input("Email address: ") or None
        if email:
            try:
                email = validate_email(email)
            except ValidationError as exc:
                print(f"Invalid email address {exc}")

        contact = Contact(first_name, last_name, phone_number, email)
        result = self.contact_list.add_contact(contact)
        print(f"Added: {contact}")
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
            contact = self.contact_list.contacts[choice - 1]
            self.contact_list.delete_contact(contact)
            print("Contact deleted successfully")
        except (IndexError, TypeError):
            print("This contact does not exist or invalid input")

    def edit_contact(self):
        if not self.contact_list.contacts:
            print("No contacts to edit")
            return

        print("\n Choose contact to edit: ")
        for idx, contact in enumerate(self.contact_list.contacts, start=1):
            print(f"{idx}. {contact}")

        try:
            choice = int(input("Choose contact: "))
            contact = self.contact_list.contacts[choice - 1]

            print("\nLeave blank to keep current values")

            confirm = input("Edit this contact? (y/n) or leave blank to cancel: ")
            if confirm.lower() != "y":
                print("Contact edit cancelled")
                return

            new_first_name = input("First name: ") or contact.first_name
            new_last_name = input("Last name: ") or contact.last_name
            new_phone_number = input("Phone number: ") or contact.phone_number
            new_email = input("Email address: ") or contact.email

            self.contact_list.edit_contact(
                contact,
                new_first_name=new_first_name,
                new_last_name=new_last_name,
                new_phone_number=new_phone_number,
                new_email=new_email,
            )
            print("Contact edited successfully")
        except (IndexError, TypeError, ValueError):
            print("This contact does not exist or invalid input")

    def handle_choice(self, choice):
        match choice:
            case "1":
                self.add_contact()
            case "2":
                self.edit_contact()
            case "3":
                self.delete_contact()
            case "4":
                self.show_contacts()
            case "5":
                print("Exiting")
                exit()

if __name__ == "__main__":
    menu = Menu()
    menu.run()

