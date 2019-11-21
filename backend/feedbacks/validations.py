from django.core import validators
from django.core.exceptions import ValidationError

def validate_content(content):
    if len(content) == 0:
        raise ValidationError("Content can't be null")
