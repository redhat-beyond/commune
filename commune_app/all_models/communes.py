from django.db import models


class Commune(models.Model):
    """
      commune object hold his:
      name
      description on the commune
      money in the wallet
    """
    name = models.TextField(max_length=150, unique=True)
    description = models.TextField(blank=True)
    wallet = models.IntegerField(default=0)

    def set_wallet(budget):
        pass
