import pytest
from commune_app.all_models.communes import Commune


NAME = "test_commune"
DESCRIPTION = "this is a description for test coomune"

NAME1 = "test_commune1"
DESCRIPTION1 = "description1"

USERNAME_IN_DB = "testUser123"


@pytest.fixture
def commune0():
    return Commune(name=NAME, description=DESCRIPTION)


@pytest.fixture
@pytest.mark.django_db()
def my_commune0(commune0):
    commune0.save()
    return commune0


@pytest.mark.django_db()
class TestComuune:

    def test_my_commune0(self, my_commune0):
        assert Commune.objects.get(id=my_commune0.id)
        assert NAME == my_commune0.name
        assert DESCRIPTION == my_commune0.description

    def test_create_delete_commune(self):
        new_commune = Commune(name=NAME, description=DESCRIPTION)
        new_commune.save()
        assert Commune.objects.get(id=new_commune.id)
        new_commune.delete()
        with pytest.raises(Exception):
            Commune.objects.get(id=new_commune.id)
