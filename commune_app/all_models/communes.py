from django.db import models
from django.core.exceptions import PermissionDenied


def validate_wallet(wallet):
    if wallet < 0:
        raise Exception("negative wallet balance")


class Commune(models.Model):
    """
    The commune object stores the following:
    Name
    Description of the commune
    Wallet balance
    """
    name = models.CharField(max_length=100, unique=True, blank=False)
    description = models.CharField(max_length=250, blank=True)
    wallet = models.IntegerField(default=0, validators=[validate_wallet])

    def clean(self) -> None:
        validate_wallet(self.wallet)
        return super().clean()

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)

    def wallet_charge(self, budget):
        """
        set wallet balance:
        To make a charge that will be deducted from the balance enter a positive,
        Enter a negative number for the wallet credit.
        """
        if self.wallet < budget:
            raise Exception("will enter negative balance")
        else:
            self.wallet -= budget

    def create_commune(self, name, description, wallet):
        my_commune = Commune(name=name, description=description, wallet=wallet)
        my_commune.save()
    def add_user(self, user, requesting_user):
        if not requesting_user.is_superuser:
            raise PermissionDenied("Only the founder can perform this action.")
        if user.commune_id is not None:
            raise Exception("User is already a member of another commune")
        user.join_commune(self)

    def remove_user(self, user, requesting_user):
        if not requesting_user.is_superuser:
            raise PermissionDenied("Only the founder can perform this action.")
        if user.commune_id != self:
            raise Exception("User is not a member of this commune")
        user.leave_commune()
