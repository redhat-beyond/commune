from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number format: '+999999999'")


class User(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=250, unique=True)
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)

    @staticmethod
    def create_user(first_name, last_name, email, phone_number):
        """"
        Method creates a new user
        param first_name: user's first name
        param last_name: user's last name
        param email: user's last email
        param phone_number: user's phone number
        """
        try:
            user = User.objects.get(email=email)
            return user
        except User.DoesNotExist:
            user = User(first_name=first_name, last_name=last_name, email=email, phone_number=phone_number)
            user.save()
            return user


class Expense(models.Model):
    title = models.CharField(max_length=50)
    budget = models.IntegerField()
    date = models.DateTimeField(default=timezone.now)
    assign = models.ForeignKey(User, on_delete=models.CASCADE)

    @staticmethod
    def create_expense(title, budget, date, assign):
        """"
        Method creates a new expense
        param title: expense's title
        param budget: expense's budget
        param date: expense's date
        param assign: expense's assign
        """
        try:
            expense = Expense.objects.get(title=title)
            return expense
        except Expense.DoesNotExist:
            expense = Expense(title=title, budget=budget, date=date, assign=assign)
            expense.save()
            return expense

    @staticmethod
    def get_expense_by_title(title):
        try:
            expense = Expense.objects.filter(title=title).order_by('date').first()
        except Expense.DoesNotExist:
            return None
        return expense
