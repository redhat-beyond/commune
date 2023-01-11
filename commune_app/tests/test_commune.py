import pytest
from commune_app.all_models.communes import Commune


NAME0 = "test_commune"
DESCRIPTION0 = "this is a description for test coomune"

NAME1 = "test_commune1"
DESCRIPTION1 = "description1"

UNVALID_NAME = "a" * 200
NEGATIVE_WALLET = -150
WALLET = 150
NAME = "parametrize"
NUMBER = 555
STRING = "abc"
DESCRIPTION = "test description"
UNVALID_DESCRIPTION = "a" * 251


@pytest.fixture
@pytest.mark.django_db()
def commune0():
    commune0 = Commune(name=NAME0, description=DESCRIPTION0, wallet=1000)
    commune0.save()
    return commune0


@pytest.mark.django_db()
class TestComuune:

    def test_my_commune0(self, commune0):
        assert Commune.objects.get(id=commune0.id)
        assert NAME0 == commune0.name
        assert DESCRIPTION0 == commune0.description

    def test_create_commune(self):
        new_commune = Commune(name=NAME1, description=DESCRIPTION1)
        new_commune.save()
        assert Commune.objects.get(id=new_commune.id)

    def test_delete_commune(self):
        new_commune = Commune.objects.filter(name=NAME1)
        new_commune.delete()
        with pytest.raises(Exception):
            Commune.objects.get(id=new_commune.id)

    def test_positive_wallet_charge(self, commune0):
        commune0.wallet_charge(800)
        assert commune0.wallet == 200

    def test_negative_wallet_charge(self, commune0):
        with pytest.raises(Exception):
            commune0.wallet_charge(1500)

    @pytest.mark.parametrize("name, wallet, description", [
        (UNVALID_NAME, WALLET, DESCRIPTION),    # long name
        (NAME, NEGATIVE_WALLET, DESCRIPTION),   # negative wallet balance
        (None, WALLET, DESCRIPTION),            # None name
        (NAME, STRING, DESCRIPTION),
        (NAME, WALLET, UNVALID_DESCRIPTION)
        ],
    )
    def test_invalid_commune_values(self, name, wallet, description):
        with pytest.raises(Exception):
            commune = Commune(name=name, wallet=wallet, description=description)
            commune.save()
