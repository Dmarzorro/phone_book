from __future__ import annotations

import phonenumbers as pn
import re
import unicodedata
import uuid
from typing import Iterable
from phonenumbers.phonenumberutil import NumberParseException

from email_validator import validate_email av _ve, EmailNotValidError

__all__ = (
    "validate_phone_number",
    "validate_email",
    "validate_name",
    "slugify_name",
    "ensure_unique_phone",
    "ensure_unique_email",
    "generate_uuid",
)

