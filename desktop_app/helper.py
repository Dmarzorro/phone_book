from __future__ import annotations

import phonenumbers as pn
import re
import unicodedata
import uuid
from typing import Iterable
from phonenumbers.phonenumberutil import NumberParseException
from email_validator import validate_email as _ve, EmailNotValidError

class ValidationError(Exception):
    def __init__(self, message: str, code: int | None = None):
        super().__init__(message)
        self.code = code

__all__ = (
    "prompt_valid",
    "validate_phone",
    "validate_email",
    "validate_name",
    "slugify_name",
    "ensure_unique_phone",
    "ensure_unique_email",
    "generate_uuid",
    "ValidationError",
)

def validate_phone(raw: str, region: str = "PL", *, strict:bool = True) -> str: # E.164 format
    raw = raw.strip()
    if not raw:
        raise ValidationError("Phone number cannot be empty")

    try:
        phone_number = pn.parse(raw, region)
    except NumberParseException:
        raise ValidationError(f"Invalid number: wrong number format") from None

    if not pn.is_possible_number(phone_number):
        raise ValidationError("Number is impossible for region (lenghth or prefix)")

    if strict and not pn.is_valid_number(phone_number):
        raise ValidationError("Number fails national validation rules")

    return pn.format_number(phone_number, pn.PhoneNumberFormat.E164)

def validate_email(raw: str) -> str:
    raw = raw.strip()
    if not raw:
        raise ValidationError("Email cannot be empty")

    try:
        res = _ve(raw, check_deliverability=False)
    except EmailNotValidError as exc:
        raise ValidationError(f"invalid mail: {exc}") from None
    return res.normalized


def validate_name(raw: str) -> str:
    value = raw.strip()
    if not value:
        raise ValidationError("Name cannot be empty")

    normalized = unicodedata.normalize("NFKC", value)

    for char in normalized:
        if char in {" ", "-", "'"}:
            continue

        if unicodedata.category(char)[0] not in ("L", "M"):
            raise ValidationError(f"Invalid character: {char!r}")

    cleaned = re.sub(r"\s+", " ", normalized)
    return cleaned


def slugify_name(raw: str) -> str:
    if raw is None:
        raise ValidationError("Name cannot be empty")
    raw = raw.strip()
    if not raw:
        raise ValidationError("Name cannot be empty")

    normalized = unicodedata.normalize("NFKD", raw)
    without_accents = "".join(
        c for c in normalized
        if not unicodedata.combining(c)
    )

    lowered = without_accents.lower()

    cleaned = re.sub(r"[^\w\s-]", "", lowered)

    slug = re.sub(r"[\s_-]+", "-", cleaned).strip("-")

    if not slug:
        raise ValidationError("Slug is empty after normalization")

    return slug

def ensure_unique_phone(raw: str, existing: Iterable[str]) -> str:
    phone = validate_phone(raw)
    normalized_existing = {validate_phone(p) for p in existing}
    if phone in normalized_existing:
        raise ValidationError("Phone number already exists")
    return phone

def ensure_unique_email(raw: str, existing: Iterable[str]) -> str:
    email = validate_email(raw).lower()

    normalized_existing = {e.lower() for e in existing}
    if email in normalized_existing:
        raise ValidationError("Email already exists")

    return email

def generate_uuid() -> str:
    return str(uuid.uuid4())

def prompt_valid(prompt: str, validator) -> str:
    while True:
        value = input(prompt)
        try:
            return validator(value)
        except ValidationError as exc:
            print(exc)
