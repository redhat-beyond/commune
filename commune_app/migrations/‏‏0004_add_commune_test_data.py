from django.db import migrations, transaction


DESCRIPTION1 = "this is description for test commune 1"
DESCRIPTION2 = "our commune want peace in the world"
DESCRIPTION3 = "Say no to violence"


class Migration(migrations.Migration):

    dependencies = [
        ('commune_app', '0003_createsuperuser'),
    ]

    def generate_commune_test_data(apps, schema_editor):
        from ..all_models.communes import Commune

        communes_test_data = [
            ('testCommune1', DESCRIPTION1, 0),
            ('world peace', DESCRIPTION2, 500),
            ('say hello dont attack', DESCRIPTION3, 1200)
        ]

        with transaction.atomic():
            for commune_name, commune_description, balance_to_start in communes_test_data:
                commune = Commune(name=commune_name, description=commune_description, wallet=balance_to_start)
                commune.save()

    operations = [
        migrations.RunPython(generate_commune_test_data),
    ]
