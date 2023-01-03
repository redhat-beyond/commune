from __future__ import unicode_literals
from django.db import migrations, transaction
from commune_app.all_models.users import User


def create_superuser(apps, schema_editor):
    with transaction.atomic():
        superuser = User(
            is_active=True, is_superuser=True, is_staff=True, username='admin', email='admin@gmail.com'
            )
        superuser.set_password('adminPassword')
        superuser.save()


class Migration(migrations.Migration):

    dependencies = [
        ('commune_app', '0003_add_user_test_data'),
    ]

    operations = [
        migrations.RunPython(create_superuser)
    ]
