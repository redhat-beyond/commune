from django.db import migrations, transaction


class Migration(migrations.Migration):

    dependencies = [
        ('commune_app', '0005_alter_user_groups_alter_user_is_active'),
    ]

    def generate_chore_test_data(apps, schema_editor):
        from ..all_models.chores import Chore
        from ..all_models.users import User
        from ..all_models.communes import Commune

        chores_test_data = [
            ('testChore1', 'discription 1', 100, False, False),
            ('testChore2', 'discription 2', 200, False, False),
            ('testChore3', 'discription 3', 300, True, False),
            ('testChore4', 'discription 4', 400, True, False),
            ('testChore5', 'discription 5', 500, True, True),
        ]

        user = User.objects.get(id=1)
        commune = Commune.objects.get(id=1)

        with transaction.atomic():
            for chore_name, description, budget, passed, completed in chores_test_data:
                chore = Chore(
                    title=chore_name,
                    description=description,
                    budget=budget,
                    assign_to=user,
                    passed=passed,
                    completed=completed,
                    commune_id=commune
                    )
                chore.save()

    operations = [
        migrations.RunPython(generate_chore_test_data),
    ]
