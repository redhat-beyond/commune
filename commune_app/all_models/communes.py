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

    def wallet_charge(self, budget):
        '''
        set wallet balance:
        To make a charge that will be deducted from the balance enter a positive,
        Enter a negative number for the wallet credit.
        '''
        if (self.wallet < budget):
            raise Exception("will enter negative balance")
        else:
            self.wallet -= budget
