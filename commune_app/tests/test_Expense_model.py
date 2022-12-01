from ..models import Expense, User
import pytest

USER1_ID = 1115799993
USER1_FIRST_NAME = "Faez"
USER1_LAST_NAME = "Zangariya"
USER1_EMAIL = "faezzangariyacs@gmail.com"
USER1_PHONE_NUMBER = "+972523324193"

EXPENSE1_TITLE = "X"
EXPENSE1_BUDGET = 100
EXPENSE1_DATE = "2011-09-01T13:20:30+03:00"

EXPENSE2_TITLE = "Y"
EXPENSE2_BUDGET = 200
EXPENSE2_DATE = "2011-09-01T13:20:30+03:00"

EXPENSE3_TITLE = "Z"
EXPENSE3_BUDGET = 300
EXPENSE3_DATE = "2011-09-01T13:20:30+03:00"


@pytest.fixture
def user1():
    return User(
        id=USER1_ID,
        first_name=USER1_FIRST_NAME,
        last_name=USER1_LAST_NAME,
        email=USER1_EMAIL,
        phone_number=USER1_PHONE_NUMBER
    )


@pytest.fixture
def expense1(user1):
    return Expense(title=EXPENSE1_TITLE, budget=EXPENSE1_BUDGET, date=EXPENSE1_DATE, assign=user1)


@pytest.fixture
def expense2(user1):
    return Expense(title=EXPENSE2_TITLE, budget=EXPENSE2_BUDGET, date=EXPENSE2_DATE, assign=user1)


@pytest.fixture
def expense3(user1):
    return Expense(title=EXPENSE3_TITLE, budget=EXPENSE3_BUDGET, date=EXPENSE3_DATE, assign=user1)


class TestExpenseModel:
    def test_new_expense(self, expense1):
        assert expense1.title == "X"
        assert expense1.budget == 100
        assert expense1.date == "2011-09-01T13:20:30+03:00"
        assert expense1.assign.first_name == "Faez"

    @pytest.mark.django_db
    def test_get_expense_by_title(self, user1, expense1, expense2, expense3):
        user1.save()
        expense1.save()
        expense2.save()
        expense3.save()
        assert Expense.get_expense_by_title("X") == expense1
        assert Expense.get_expense_by_title("Y") == expense2
        assert Expense.get_expense_by_title("Z") == expense3
        assert Expense.get_expense_by_title("X").budget == 100
        assert Expense.get_expense_by_title("Y").budget == 200
        assert Expense.get_expense_by_title("Z").budget == 300
