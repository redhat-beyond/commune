from django.db import migrations , models
from django.contrib.postgres.fields import ArrayField


class Migration(migrations.Migration):
    dependencies = [

    ]

    def generate_data(apps):
        operations = [
            migrations.CreateModel(
                name='Commune',
                fields=[
                    ('users',ArrayField(models.IntegerField())), # Place holder
                    ('wallet',models.IntegerField()), # Place holder
                    ('chores',ArrayField(models.IntegerField())), # Place holder
                    ('expenses',ArrayField(models.IntegerField())), # Place holder
                    ('decisions',ArrayField(models.IntegerField())), # Place holder
                    ('name',models.CharField(max_length=50))
                ],
            ),
        ]


    operations = [
        migrations.RunPython(generate_data),
    ]

