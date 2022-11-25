from django.db import models
from django.utils import timezone
# Create your models here.

class Expense(models.Model):
    title = models.CharField( max_length=50)
    budget = models.IntegerField()
    date = models.DateTimeField(default=timezone.now)
    #assign = models.ForeignKey(User, on_delete=models.CASCADE)
    E_id = models.IntegerField(primary_key=True)

    def __str__(self):
        return "id: %d | title: %s | budget: %d | date:" % (self.E_id,self.title, self.budget) + self.date
        