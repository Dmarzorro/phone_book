import uuid
from datetime import datetime

class Contact:
    def __init__(self, first_name, last_name, phone_number, email=None, tags=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.tags = tags if tags else []
        self.created_at = datetime.now()
        self.id = uuid.uuid4()

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.phone_number})"

    def __eq__(self, other):
        if not isinstance(other, Contact):
            return False
        return (
            self.first_name == other.first_name
            and self.last_name == other.last_name
            and self.phone_number == other.phone_number
            and self.email == other.email
        )

class ContactList:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        if contact not in self.contacts:
            self.contacts.append(contact)
            return "Contact added successfully"
        else:
            return "This contact already exists"

    def show_contacts(self):
        if not self.contacts:
            return "No contacts available."

        result = []
        for contact in self.contacts:
            result.append(f"{contact.first_name} {contact.last_name} {contact.phone_number}")

        return "\n".join(result)

    def delete_contact(self, contact):
        if contact in self.contacts:
            self.contacts.remove(contact)
            return "Contact deleted successfully"
        else:
            return "This contact does not exist"

    def edit_contact(self, contact, new_first_name=None, new_last_name=None, new_email=None, new_phone_number=None):
        if new_first_name:
            contact.first_name = new_first_name
        if new_last_name:
            contact.last_name = new_last_name
        if new_email:
            contact.email = new_email
        if new_phone_number:
            contact.phone_number = new_phone_number
