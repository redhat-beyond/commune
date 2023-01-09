from django.db import models


MAX_LEN_NAME = 100


def validate_wallet(wallet):
    if (wallet < 0):
        raise Exception("negative wallet balance")


def validate_name(name):
    if (len(name) > MAX_LEN_NAME):
        raise Exception("long name")


class Commune(models.Model):
    """
    The commune object stores the following: 
    Name
    Description of the commune
    Wallet balance
    """
    name = models.TextField(max_length=MAX_LEN_NAME, unique=True, validators=[validate_name], blank=False)
    description = models.TextField(blank=True)
    wallet = models.IntegerField(default=0, validators=[validate_wallet])

    def clean(self) -> None:
        validate_wallet(self.wallet)
        validate_name(self.name)
        return super().clean()

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)

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
