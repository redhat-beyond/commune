import pytest
from commune_app.models import Chore, User


LONG_FIELD = "a" * 301
NEGATIVE_WALLET = -150

TITLE_NOT_IN_DB = "WTF"

TITLE = "Gardener"
DATE = (2000, 1, 15)
BUDGET = 0
DESCRIPTION = "take care of garden"
ASSIGN_TO = "tom"
PASSED = False
COMPLETED = False


USER1_ID = 206609999
USER1_USERNAME = "Elias"
USER1_PASSWORD = "Wtf123"
USER1_FIRST_NAME = "Elias"
USER1_LAST_NAME = "Assy"
USER1_EMAIL = "eliasakahaxor@gmail.com"

CHORE_TITLE = "Dishes"
CHORE_DATE = (1997, 10, 19)
CHORE_BUDGET = 30
CHORE_DESCRIPTION = "Clean the Dishes"
CHORE_ASSIGN_TO = "Elias"
CHORE_PASSED = True
CHORE_COMPLETED = True


@pytest.fixture
def user0():
    user0 = User(
        username=USER1_USERNAME,
        password=USER1_PASSWORD,
        first_name=USER1_FIRST_NAME,
        last_name=USER1_LAST_NAME,
        email=USER1_EMAIL
    )
    user0.save()
    return user0


@pytest.fixture
def chore0(user0):
    return Chore(
        title=CHORE_TITLE,
        description=CHORE_DESCRIPTION,
        date=CHORE_DATE,
        budget=CHORE_BUDGET,
        assign_to=user0,
        passed=CHORE_PASSED,
        completed=CHORE_COMPLETED
    )


@pytest.fixture
@pytest.mark.django_db()
def persist_chore(chore0):
    chore0.save()
    return chore0


@pytest.mark.django_db()
class TestChoreModel:

    def test_new_chore(self, chore0):
        assert chore0.title == CHORE_TITLE
        assert chore0.description == CHORE_DESCRIPTION
        assert chore0.date == CHORE_DATE
        assert chore0.budget == CHORE_BUDGET
        assert chore0.assign_to.first_name == "Elias"
        assert chore0.passed == CHORE_PASSED
        assert chore0.completed == CHORE_COMPLETED

    def test_delete_chore(self, persist_chore):
        persist_chore.delete()
        assert persist_chore not in Chore.objects.all()

    def test_title_not_in_db(self):
        with pytest.raises(Exception):
            Chore.objects.get(title=TITLE_NOT_IN_DB)

    def test_create_chore(self, user0):
        new_chore = Chore(
            title=TITLE,
            description=DESCRIPTION,
            date=DATE,
            budget=BUDGET,
            assign_to=user0,
            passed=PASSED,
            completed=COMPLETED
        )
        new_chore.save()
        assert new_chore in Chore.objects.all()

    @pytest.mark.parametrize("title, description, date, budget, assign_to, passed, completed", [
        (LONG_FIELD, DESCRIPTION, DATE, BUDGET, ASSIGN_TO, PASSED, COMPLETED),       # long title
        (TITLE, LONG_FIELD, DATE, BUDGET, ASSIGN_TO, PASSED, COMPLETED),      # long description
        (CHORE_TITLE, DESCRIPTION, DATE, BUDGET, ASSIGN_TO, PASSED, COMPLETED),      # title name taken

        ],
    )
    def test_invalid_chore_values(self, title, description, date, budget, assign_to, passed, completed, persist_chore):
        with pytest.raises(Exception):
            chore = Chore(
                title=title,
                description=description,
                date=date,
                budget=budget,
                assign_to=assign_to,
                passed=passed,
                completed=completed
            )
            chore.save()
