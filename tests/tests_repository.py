import pytest
from desktop_app.repository import add_contact, delete_contact, get_all_contacts
from desktop_app.helper import ValidationError
from desktop_app.models import Contact, db
from uuid import UUID

def test_add_contact_success(test_db):
    contact = add_contact(
        first_name="Yaroslav",
        last_name="Mazur",
        phone="+48572430878",
        email="somethinghere@gmail.com"
    )
    assert isinstance(contact, Contact)
    assert contact.first_name == "Yaroslav"
    assert contact.last_name == "Mazur"
    assert contact.phone == "+48572430878"
    assert contact.email == "somethinghere@gmail.com"
    assert isinstance(contact.id, UUID)

    contact = get_all_contacts()
    assert len(contact) == 1

def test_add_contact_phone(test_db):
    add_contact("Ivan", "Drago", "+48588232998", "somethinghere@gmail.com")

    with pytest.raises(ValidationError):
        add_contact("Ivan", "Drago", "+48588232998", "somethinghere@gmail.com")


def test_add_contact_email(test_db):
    add_contact("Ivan", "Drago", "+48912345678", "somethinghere@gmail.com")

    with pytest.raises(ValidationError):
        add_contact("Ivan", "Drago", "+48912345678", "somethingheregmail.com")

def test_delete_contact(test_db):
    contact = add_contact("Ivan", "Drago", "+48912345678", "somethinghere@gmail.com")
    contacts = get_all_contacts()
    assert any(c.id == contact.id for c in contacts)

    deleted = delete_contact(contact.id)
    assert deleted is True

    contacts_after = get_all_contacts()
    assert all(c.id != contact.id for c in contacts_after)