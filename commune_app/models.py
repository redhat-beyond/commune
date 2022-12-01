from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

# regex to filter valid phone numbers
phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number format: '+999999999'")


class User(AbstractUser):
    id = models.IntegerField(unique=True, primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=250, unique=True)
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)


class Expense(models.Model):
    title = models.CharField(max_length=50)
    budget = models.IntegerField()
    date = models.DateTimeField(default=timezone.now)
    assign = models.ForeignKey(User, on_delete=models.CASCADE)

    # returns an expense matching the title given as paramater
    @staticmethod
    def get_expense_by_title(title):
        try:
            expense = Expense.objects.filter(title=title).order_by('date').first()
        except Expense.DoesNotExist:
            return None
        return expense

class Commune(Models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    users = models.ManyToManyField(User)
    expenses = models.ManyToManyField(Expense)
    wallet = models.IntegerField()
    chores = ArrayField(IntegerField())
    decisions = models.ManyToManyField(Decision)
    name = models.TextField()

    @staticmethod
    def fetch_commune_stats(id):
        try:
            commune = commune.objects.filter(id=id)
        except Commune.DoesNotExist:
            return None
        return commune
