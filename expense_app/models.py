from django.db import models
from django.utils import timezone
# Create your models here.


class Expense(models.Model):
    title = models.CharField(max_length=50)
    budget = models.IntegerField()
    date = models.DateTimeField(default=timezone.now)
    # assign = models.ForeignKey(User, on_delete=models.CASCADE)
    E_id = models.IntegerField(primary_key=True)

    def __str__(self):
<<<<<<< HEAD
        return "id: %d | title: %s | budget: %d | date:" % (self.E_id, self.title, self.budget) + " " + self.date
=======
        return "id: %d | title: %s | budget: %d | date:" % (self.E_id,self.title, self.budget) + " " + self.date

>>>>>>> 3f0c0a8aac83f40b815044ff866b96375187ee26
