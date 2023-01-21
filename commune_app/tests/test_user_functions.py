import pytest
from commune_app.all_models.users import User
from commune_app.all_models.communes import Commune
from commune_app.all_models.chores import Chore
from commune_app.all_models.votes import Vote

USER_NAME0 = "user0"
PASSWORD0 = "123456"
FIRST_NAME0 = "user"
LAST_NAME0 = "usery"
EMAIL0 = "user@gmail.com"
ID0 = 123456789

NAME0 = "test_commune"
DESCRIPTION0 = "this is a description for test coomune"
COMMUNE_ID = 4222

TITLE = "Gardener"
DATE = (2000, 1, 15)
BUDGET = 0
DESCRIPTION = "take care of garden"
ASSIGN_TO = "tom"
PASSED = True
COMPLETED = False

NOT_PASSED = False


@pytest.fixture
@pytest.mark.django_db()
def user0(commune0):
    user0 = User(
        username=USER_NAME0,
        password=PASSWORD0,
        id=ID0,
        first_name=FIRST_NAME0,
        last_name=LAST_NAME0,
        email=EMAIL0
    )
    user0.save()
    return user0


@pytest.fixture
@pytest.mark.django_db()
def commune0():
    commune0 = Commune(name=NAME0, description=DESCRIPTION0, id=COMMUNE_ID)
    commune0.save()
    return commune0


@pytest.fixture
@pytest.mark.django_db()
def chore0(user0):
    chore0 = Chore(
        title=TITLE,
        description=DESCRIPTION,
        date=DATE,
        budget=BUDGET,
        assign_to=user0,
        passed=PASSED,
        completed=COMPLETED
    )
    chore0.save()
    return chore0


@pytest.fixture
@pytest.mark.django_db()
def chore1(user0):
    chore1 = Chore(
        title=TITLE,
        description=DESCRIPTION,
        date=DATE,
        budget=BUDGET,
        assign_to=user0,
        passed=NOT_PASSED,
        completed=COMPLETED
    )
    chore1.save()
    return chore1


@pytest.mark.django_db()
class TestUserFunctions:

    def test_join_commune(self, user0, commune0):
        assert user0 not in User.objects.filter(commune_id=commune0)
        user0.join_commune(commune0.id)
        assert user0.commune_id == Commune.objects.filter(id=commune0.id).first()
        assert user0 in User.objects.filter(commune_id=commune0)

    def test_leave_commune(self, user0, commune0):
        user0.join_commune(commune0.id)
        assert user0 in User.objects.filter(commune_id=commune0)
        user0.leave_commune()
        assert user0 not in User.objects.filter(commune_id=commune0)

    def test_execute_chore(self, chore0, user0):
        user0.join_commune(COMMUNE_ID)
        assert not chore0.completed
        chore0.execute_chore(chore0.id, user0.id)
        choren = Chore.objects.filter(id=chore0.id).first()
        assert choren.completed

    def test_user_vote(self, chore1, user0, commune0):
        assert not chore1.passed
        user0.join_commune(commune0.id)
        Vote.create_new_vote(voting_user=user0, voted_chore=chore1, vote_bool=True)
        vote = Vote.objects.filter(user=user0, chore=chore1).first()
        assert vote in Vote.objects.all()
