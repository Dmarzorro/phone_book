from desktop_app.repository import (
    add_contact,
    get_all_contacts,
    edit_contact,
    delete_contact,
)
from desktop_app.helper import *
from desktop_app.file_export import export_contacts_to_md, export_contacts_to_txt, export_contacts_to_csv

class Menu:
    def __init__(self):
        pass

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
        print('5. Export Contacts')
        print('6. Exit')

    def show_contacts(self):
        contacts = get_all_contacts()
        if not contacts:
            print("No contacts found")
            return

        for idx, c in enumerate(contacts, 1):
            print(f"{idx}. {c}  —  ID: {str(c.id)[:8]}…")

    def add_contact(self):
        try:
            first_name = prompt_valid("First name: ", validate_name)
            last_name = prompt_valid("Last name: ", validate_name)
            phone = prompt_valid("Phone number: ", validate_phone)
            email = prompt_valid("Email: ", validate_email)
        except ValidationError as exc:
            print(f"Error: {exc}")
            return

        try:
            contact = add_contact(
                first_name=first_name,
                last_name=last_name,
                phone=phone,
                email=email,
            )
            print(f"Contact added: {contact}")
        except ValidationError as exc:
            print(f"Error: {exc}")

    def delete_contact_by_id(self):
        contacts = get_all_contacts()
        if not contacts:
            print("No contacts to delete")
            return

        print("\n Choose contact to delete: ")
        for idx, contact in enumerate(contacts, start=1):
            print(f"{idx}. {contact}")

        try:
            choice = int(input("Choose contact: "))
            if choice <= 0 or choice > len(contacts):
                raise IndexError("Invalid choice")

            contact = contacts[choice - 1]
            print(f"Deleting contact: {contact}, \n are you sure? (y/n)")
            confirm = input("Enter y to confirm:")
            if confirm.lower().strip() != "y":
                print("Contact deletion cancelled")
                return

            if delete_contact(contact.id):
                print("Contact deleted successfully")
            else:
                print("Contact already removed")
        except (ValueError, IndexError):
            print("Invalid choice")

    def edit_contact(self):
        contacts = get_all_contacts()
        if not contacts:
            print("No contacts to edit")
            return

        print("\n Choose contact to edit: ")
        for idx, contact in enumerate(contacts, start=1):
            print(f"{idx}. {contact}")

        try:
            choice = int(input("Choose contact to edit: "))
            if choice <= 0 or choice > len(contacts):
                raise IndexError("Invalid choice")

            contact = contacts[choice - 1]

            confirm = input(f"Editing contact: {contact}, \n are you sure? (y/n)")
            if confirm.lower().strip() != "y":
                print("Contact edit cancelled")
                return

            new_first = input("First name: ") or None
            new_last = input("Last name: ") or None
            new_phone = input("Phone number: ") or None
            new_email = input("Email address: ") or None

            ok = edit_contact(contact.id, first_name=new_first, last_name=new_last, phone=new_phone, email=new_email)

            print("Contact edited successfully" if ok else "Contact not found or invalid input")

        except (ValueError, IndexError):
            print("Invalid choice")

        except ValidationError as ve:
            print(f"Error: {ve}")

    def export_contacts(self):
        print("Export format: 1. CSV  2. Markdown  3. TXT")
        choice = input("Choose format: ").strip()
        match choice:
            case "1":
                file_path = get_unique_filename("contacts", "csv")
                export_contacts_to_csv(file_path)
            case "2":
                file_path = get_unique_filename("contacts", "md")
                export_contacts_to_md(file_path)
            case "3":
                file_path = get_unique_filename("contacts", "txt")
                export_contacts_to_txt(file_path)
            case _:
                print("Invalid format")

    def handle_choice(self, choice_raw: str) -> None:
        choice = choice_raw.strip().lower()
        match choice:
            case "1":
                self.add_contact()
            case "2":
                self.edit_contact()
            case "3":
                self.delete_contact_by_id()
            case "4":
                self.show_contacts()
            case "5":
                self.export_contacts()
            case "6":
                print("Exiting")
                exit()

if __name__ == "__main__":
    menu = Menu()
    menu.run()

