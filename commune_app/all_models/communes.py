from django.db import models
from .users import User
from .chores import Chore
from .votes import Vote


class Commune(models.Model):
    """
      add something
    """
    id = models.IntegerField(unique=True, primary_key=True, auto_created=True)
    users = models.ManyToManyField(User)
    votes = models.ForeignKey(Vote, on_delete=models.CASCADE)
    chores = models.ForeignKey(Chore, on_delete=models.CASCADE)
    
    wallet = models.IntegerField()
    name = models.TextField()

    @staticmethod
    def fetch_commune_stats(id):
        try:
            commune = commune.objects.filter(id=id)
        except Commune.DoesNotExist:
            return None
        return commune