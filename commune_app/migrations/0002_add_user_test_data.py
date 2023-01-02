from django.db import migrations, transaction


class Migration(migrations.Migration):

    dependencies = [
        ('commune_app', '0001_initial'),
    ]

    def generate_user_test_data(apps, schema_editor):
        from ..all_models.users import User

        users_test_data = [
            ('testUser123', 'testUser1@mta.ac.il', 'PasswordU$er123', '123'),
            ('testUser234', 'testUser2@mta.ac.il', 'PasswordU$er456', '234'),
            ('testUser345', 'testUser3@mta.ac.il', 'PasswordU$er789', '345')
        ]

        with transaction.atomic():
            for user_name, user_email, user_password, user_id in users_test_data:
                user = User(username=user_name, email=user_email, password=user_password, id=user_id)
                user.set_password(user_password)
                user.save()

    operations = [
        migrations.RunPython(generate_user_test_data),
    ]
