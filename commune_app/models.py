from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


phone_regax = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="phone number format: '+999999999'")


class User(AbstractUser):
    id = models.IntegerField(unique=True, primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=250, unique=True)
    phone_number = models.CharField(validators=[phone_regax], max_length=17, blank=True)
