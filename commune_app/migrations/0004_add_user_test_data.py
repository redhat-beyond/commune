from django.db import migrations, transaction


class Migration(migrations.Migration):

    dependencies = [
        ('commune_app', '0003_add_commune_test_data'),
    ]

    def generate_user_test_data(apps, schema_editor):
        from ..all_models.users import User
        from ..all_models.communes import Commune

        users_test_data = [
            ('testUser1', 'testUser1@telhai.ac.il', 'PasswordU$er1', '1'),
            ('testUser2', 'testUser2@telhai.ac.il', 'PasswordU$er2', '2'),
            ('testUser3', 'testUser3@telhai.ac.il', 'PasswordU$er3', '3'),
            ('testUser4', 'testUser4@telhai.ac.il', 'PasswordU$er4', '4'),
            ('testUser5', 'testUser5@telhai.ac.il', 'PasswordU$er5', '5'),
            ('testUser6', 'testUser6@telhai.ac.il', 'PasswordU$er6', '6'),
            ('testUser7', 'testUser7@telhai.ac.il', 'PasswordU$er7', '7'),
            ('testUser8', 'testUser8@telhai.ac.il', 'PasswordU$er8', '8'),
        ]

        commune = Commune.objects.get(id=1)

        with transaction.atomic():
            for user_name, user_email, user_password, user_id in users_test_data:
                user = User(username=user_name, email=user_email, password=user_password, id=user_id)
                user.join_commune(commune_id=commune.id)
                user.save()

    operations = [
        migrations.RunPython(generate_user_test_data),
    ]
