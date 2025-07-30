from peewee import IntegrityError
from uuid import uuid4, UUID
from typing import List

from models import Contact, db
from helper import (
    validate_name,
    validate_phone,
    validate_email,
    ValidationError,
)

def get_all_contacts() -> List[Contact]:
    return list(Contact.select().order_by(Contact.created_at.desc()))


def add_contact(first_name: str, last_name: str, phone: str, email:str = None) -> Contact:
    """
    Adds a new contact with the provided details to the contact list. This operation
    creates an instance of the `Contact` class using the specified inputs and includes
    optional handling for additional email addresses if applicable.
    """
    #validation
    first_name = validate_name(first_name)
    last_name = validate_name(last_name)
    phone_number = validate_phone(phone)

    #saving to database
    if email:
        email = validate_email(email)
    try:
        with db.atomic():
            contact = Contact.create(
                id=uuid4(),
                first_name=first_name,
                last_name=last_name,
                phone=phone,
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

def edit_contact(contact_id: UUID,
                 first_name:str |  None = None,
                 last_name: str |  None = None,
                 phone: str |      None = None,
                 email: str |      None = None,
) -> bool:
    """
    Edits an existing contact in the contact database. Allows updating specific
    fields such as first name, last name, phone number, and email address. All
    updates are optional, and only provided non-None parameters will be updated.
    The function returns a boolean value indicating whether the contact update
    was successful.
    """
    try:
        contact = Contact.get(Contact.id == contact_id)
    except Contact.DoesNotExist:
        return False

    #validation with helper
    if first_name is not None:
        first_name = validate_name(first_name)
    if last_name is not None:
        last_name = validate_name(last_name)
    if phone is not None:
        phone = validate_phone(phone)
    if email is not None:
        email = validate_email(email)

    #changing data
    if first_name is not None: contact.first_name = first_name
    if last_name is not None: contact.last_name = last_name
    if phone is not None: contact.phone = phone
    if email is not None: contact.email = email

    #saving data
    try:
        with db.atomic():
            contact.save()
    except IntegrityError as exc:
        raise ValidationError(f"Contact already exists: {exc}") from None

    return True

