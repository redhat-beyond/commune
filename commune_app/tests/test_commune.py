import pytest
from commune_app.all_models.communes import Commune


NAME = "test_commune"
DESCRIPTION = "this is a description for test coomune"

NAME1 = "test_commune1"
DESCRIPTION1 = "description1"


@pytest.fixture
@pytest.mark.django_db()
def commune0():
    commune0 = Commune(name=NAME, description=DESCRIPTION)
    commune0.save()
    return commune0


@pytest.mark.django_db()
class TestComuune:

    def test_my_commune0(self, commune0):
        assert Commune.objects.get(id=commune0.id)
        assert NAME == commune0.name
        assert DESCRIPTION == commune0.description

    def test_create_delete_commune(self):
        new_commune = Commune(name=NAME, description=DESCRIPTION)
        new_commune.save()
        assert Commune.objects.get(id=new_commune.id)
        new_commune.delete()
        with pytest.raises(Exception):
            Commune.objects.get(id=new_commune.id)

    def test_wallet(self, commune0):
        commune0.wallet_charge(-1000)
        assert commune0.wallet == 1000
        commune0.wallet_charge(800)
        assert commune0.wallet == 200
        with pytest.raises(Exception):
            commune0.wallet_charge(300)
