from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


phone_regax = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="phone number format: '+999999999'")


class User(AbstractUser):
    id = models.IntegerField(unique=True, primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=250, unique=True)
    phone_number = models.CharField(validators=[phone_regax], max_length=17, blank=True)
# remove from comment after marge and and enter to the class the next 2 lines:
# chores = models.ForeignKey(Chore, on_delete=models.CASCADE)
# expenses = models.ForeignKey(Expense, on_delete=models.CASCADE)

    @staticmethod
    def create_user(id, first_name, last_name, email, phone_number):
        """"
        Method creates a new user
        param id: user's id
        param first_name: user's first name
        param last_name: user's last name
        param email: user's last email
        param phone_number: user's phone number
        """
        try:
            user = User.objects.get(id=id)
            return user
        except User.DoesNotExist:
            user = User(id=id, first_name=first_name, last_name=last_name, email=email, phone_number=phone_number)
            user.save()
            return user
