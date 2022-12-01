from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField


class Commune(Models.Model):
    users = ArrayField(AbstractUser)
    wallet = models.IntegerField()  #Place holder until relevant models are merged
    chores = ArrayField(IntegerField()) #Place holder until relevant models are merged
    expenses = ArrayField(IntegerField()) #Place holder until relevant models are merged
    decisions = ArrayField(IntegerField()) #Place holder until relevant models are merged
    name = models.TextField()
