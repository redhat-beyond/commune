from django.db import models
from . import users


class Chore(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    budget = models.DecimalField(max_digits=7, decimal_places=2, null=True)
    assign = models.ForeignKey(users, on_delete=models.CASCADE)
    description = models.TextField(max_length=300)

    def __str__(self):
        return self.title

    def snippet(self):
        return self.description[:50] + '...'
