from django.db import models


class User(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250, unique=True)
    phone_number = models.IntegerField()
# remove from comment after marge and and enter to the class the next 2 lines:
# chores = models.ForeignKey(Chore, on_delete=models.CASCADE)
# expenses = models.ForeignKey(Expense, on_delete=models.CASCADE)
