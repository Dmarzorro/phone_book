from __future__ import annotations

import phonenumbers as pn
import re
import unicodedata
import uuid
from typing import Iterable
from phonenumbers.phonenumberutil import NumberParseException

__all__ = (
    "validate_phone",
    "validate_email",
    "validate_name",
    "slugify_name",
    "ensure_unique_phone",
    "ensure_unique_email",
    "generate_uuid",
)

from rest_framework.exceptions import ValidationError


def validate_phone(raw: str, region: str = "PL") -> str:
    raw = raw.strip()
    if not raw:
        raise ValidationError("Phone number cannot be empty")

    try:
        phone_number = pn.parse(raw, region)
    except NumberParseException as exception:
        raise ValueError(f"Invalid phone number format {exception}") from None

    if not pn.is_possible_number(phone_number):
        raise ValidationError("Number is impossible for region (lenghth or prefix)")

def validate_email(raw: str) -> str:

def validate_name(raw: str) -> str:

def slugify_name(raw: str) -> str:

def ensure_unique_phone(raw: str) -> str:

def ensure_unique_email(raw: str) -> str:

def generate_uuid():



