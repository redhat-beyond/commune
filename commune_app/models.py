from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import validate_email
from django.core.exceptions import ValidationError


def validate_email_addr(email):
    try:
        validate_email(email)
    except ValidationError:
        raise ValidationError('Email is not valid')


class User(AbstractUser):
    '''
    we use the field of Abstructuser(the required):
    id
    username
    password
    first_name
    last_name
    email

    we add:
    validator for email
    '''
    email = models.EmailField(unique=True, validators=[validate_email_addr])

    def vote_on_decision(decision_id):
        pass

    def add_decision(args):
        pass

    def execute_chore():
        pass
