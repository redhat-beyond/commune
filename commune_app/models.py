from django.db import models
from django.utils import timezone


class Expense(models.Model):
    title = models.CharField(max_length=50)
    budget = models.IntegerField()
    date = models.DateTimeField(default=timezone.now)
    assign = models.ForeignKey(User, on_delete=models.CASCADE)
    E_id = models.IntegerField(primary_key=True)
