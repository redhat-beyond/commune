from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ObjectDoesNotExist


class User(AbstractUser):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250, unique=True)
    phone_number = models.IntegerField()

    @staticmethod
    def create_user(first_name, last_name, email, phone_number):
        user = Expense(first_name=first_name, last_name=last_name, email=email, phone_number=phone_number)
        user.save()
        return user
    
class Expense(models.Model):
    title = models.CharField(max_length=50)
    budget = models.IntegerField()
    date = models.DateTimeField(default=timezone.now)
    assign = models.ForeignKey(User, on_delete=models.CASCADE)
    
    @staticmethod
    def create_expense(title, budget, date, assign):
        expense = Expense(title=title, budget=budget, date=date, assign=assign)
        expense.save()
        return expense

    @staticmethod
    def get_expense_by_title(title):
        try:
            expense = Expense.objects.filter(title=title).order_by('date').first()
        except ObjectDoesNotExist:
            return None
        return expense

    @staticmethod
    def get_AllExpenses_by_user(title):
        try:
            expenses = Expense.objects.all().filter(title=title).order_by('date').first()
        except ObjectDoesNotExist:
            return None
        return expenses
