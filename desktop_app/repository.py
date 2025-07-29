from peewee import IntegrityError
from uuid import uuid4, UUID
from typing import Optional

from desktop_app.helper import ValidationError
from models import Contact, db
from helper import (
    validate_name,
    validate_phone,
    validate_email,
    ValidationError,
)

def add_contact(first_name: str, last_name: str, phone: str, email: Optional[str] = None) -> Contact:
    """
    Adds a new contact with the provided details to the contact list. This operation
    creates an instance of the `Contact` class using the specified inputs and includes
    optional handling for additional email addresses if applicable.
    """
    #validation
    first_name = validate_name(first_name)
    last_name = validate_name(last_name)
    phone = validate_phone(phone)

    #saving to database
    if email:
        email = validate_email(email)
    try:
        with db.atomic():
            contact = Contact.creat(
                id=uuid4(),
                first_name=first_name,
                last_name=last_name,
                phone_number=phone,
                email=email,
            )
            return contact
    except IntegrityError as exc:
        raise ValidationError(f"Contact already exists: {exc}")

def delete_contact(contact_id: UUID) -> bool:
    """
    Deletes a contact identified by the given UUID.
    This function removes a contact from a database or data structure using the
    provided unique identifier. It ensures the contact associated with the
    provided ``contact_id`` is deleted and confirms the operation was successful.
    """
    try:
        with db.atomic():
            contact = Contact.get(Contact.id ==contact_id)
            contact.delete_instance()
        return True
    except Contact.DoesNotExist:
        return False
