from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from commune_app.all_models.communes import Commune



def validate_email_addr(email):
    try:
        validate_email(email)
    except ValidationError:
        raise ValidationError('Email is not valid')


class User(AbstractUser):
    '''
    Inherits fields from AbstractUser:
    id
    username
    password
    first_name
    last_name
    email

    added:
    Email validation functionality for user details
    commune id
    '''
    email = models.EmailField(unique=True, validators=[validate_email_addr])
    commune_id = models.ForeignKey(Commune, on_delete=models.CASCADE, null=True, blank=True)

    def clean(self) -> None:
        validate_email(self.email)
        return super().clean()

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)

    def join_commune(self, commune_id):
        if (self.commune_id is not None and self.commune_id != commune_id):
            raise Exception("already partner in another commune")
        self.commune_id = commune_id

    def leave_commune(self):
        if (self.commune_id is not None):
            self.commune_id = None
