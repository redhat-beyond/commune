import pytest
from commune_app.models import User


FIRST_NAME = "user"
LAST_NAME = "usery"
EMAIL = "user@gmail.com"
PHONE_NUM = "+972544651892"
ID = "123456789"
ID_NOT_IN_DB = "987654321"

NOT_VALID_EMAIL = "userusery"
NOT_VALID_PHONE = "+9725218773!@#$%^&*()24"


@pytest.fixture
@pytest.mark.django_db()
def user0():
    return User.objects.create(id=ID, first_name=FIRST_NAME, last_name=LAST_NAME, email=EMAIL, phone_number=PHONE_NUM)


@pytest.mark.django_db()
class TestUser:

    def test_user0(self, user0):
        assert User.objects.get(id=ID)
        assert ID == user0.id
        assert FIRST_NAME == user0.first_name
        assert LAST_NAME == user0.last_name
        assert EMAIL == user0.email
        assert PHONE_NUM == user0.phone_number

    def test_ID_not_db(self):
        with pytest.raises(Exception):
            User.objects.get(id=ID_NOT_IN_DB)

    # def test_unvalid_arguments(self):
    #     pass                                 add soon more test
    #                                          check why validators doesn't work
