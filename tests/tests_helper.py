import pytest
from desktop_app.helper import validate_phone, ValidationError, validate_name, validate_email

# --- Phone tests ---

def test_validate_phone_ok():
    assert validate_phone('+48572220778') == '+48572220778'
    assert validate_phone('572220778') == '+48572220778'

def test_validate_phone_fail():
    with pytest.raises(ValidationError):
        validate_phone("123-abc")

def test_validate_phone_empty():
    with pytest.raises(ValidationError):
        validate_phone("")

# --- Name tests ---

def test_validate_name_ok():
    assert validate_name("Vaictus") == "Vaictus"

def test_validate_name_fail():
    with pytest.raises(ValidationError):
        validate_name("123-abc")

def test_validate_name_empty():
    with pytest.raises(ValidationError):
        validate_name("")

def test_validate_name_ok_with_spaces():
    assert validate_name(" Vaictus ") == "Vaictus"

# --- Email tests ---

def test_validate_email_ok():
    assert validate_email("jaroslawmazur63@gmail.com") == "jaroslawmazur63@gmail.com"

def test_validate_email_fail():
    with pytest.raises(ValidationError):
        validate_email("<email>")

def test_validate_email_empty():
    with pytest.raises(ValidationError):
        validate_email("")

def test_validate_email_without_at():
    with pytest.raises(ValidationError):
        validate_email("jaroslawmazur63gmail.com")
