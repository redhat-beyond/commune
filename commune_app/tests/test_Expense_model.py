from ..models import Expense, User
import pytest


class TestExpenseModel:
    @pytest.mark.django_db
    def test_new_expense(self):
        expense = Expense(title="buying some food", budget="150", date="2011-09-01T13:20:30+03:00", assign=User(first_name="Faez", last_name="Zangariya", email="faezzangariyacs@gmail.com", phone_number="+972523324193"))
        assert expense.title == "buying some food"
        assert expense.budget == "150"
        assert expense.date == "2011-09-01T13:20:30+03:00"
        assert expense.assign.first_name == "Faez"

    @pytest.mark.django_db
    def test_create_expense(self):
        expense = Expense.create_expense(title="Laundry", budget="200", date="2011-09-01T13:20:30+03:00", assign=User.create_user(first_name="Ron", last_name="Tur", email="rontur@gmail.com", phone_number="+972523324193"))
        assert expense.title == "Laundry"
        assert expense.budget == "200"
        assert expense.date == "2011-09-01T13:20:30+03:00"
        assert expense.assign.first_name == "Ron"

    @pytest.mark.django_db
    def test_get_expense_by_title(self):
        currU = User.create_user(first_name="ofir", last_name="tza", email="ofirtza@gmail.com", phone_number="+972523324193")
        expense1 = Expense.create_expense(title="X", budget="100", date="2011-09-01T13:20:30+03:00", assign=currU)
        expense2 = Expense.create_expense(title="Y", budget="200", date="2011-09-01T13:20:30+03:00", assign=currU)
        expense3 = Expense.create_expense(title="Z", budget="300", date="2011-09-01T13:20:30+03:00", assign=currU)
        assert Expense.get_expense_by_title("X") == expense1
        assert Expense.get_expense_by_title("Y") == expense2
        assert Expense.get_expense_by_title("Z") == expense3
        assert Expense.get_expense_by_title("X").budget == 100
        assert Expense.get_expense_by_title("Y").budget == 200
        assert Expense.get_expense_by_title("Z").budget == 300
