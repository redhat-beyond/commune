from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator, validate_email
from django.core.exceptions import ValidationError


phone_regax = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="phone number format: '+999999999'")


def validate_email_addr(email):
    try:
        validate_email(email)
    except ValidationError:
        raise ValidationError('Email is not valid')


class User(AbstractUser):
    id = models.IntegerField(unique=True, primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=250, unique=True, validators=[validate_email_addr])
    phone_number = models.CharField(validators=[phone_regax], max_length=17, blank=True)
