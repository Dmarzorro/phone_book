from datetime import datetime

class Contact:
    def __init__(self, first_name, last_name, phone_number, email=None, tags=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.tags = tags if tags else []
        self.created_at = datetime.now()
        self.id = id(self)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.phone_number})"

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


