from django.db import models
from commune_app.all_models.users import User
from commune_app.all_models.communes import Commune


class Chore(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=300)
    date = models.DateTimeField(auto_now_add=True)
    budget = models.DecimalField(max_digits=7, decimal_places=2, null=True)
    assign_to = models.ForeignKey(User, on_delete=models.CASCADE)
    passed = models.BooleanField()
    completed = models.BooleanField()
    commune_id = models.ForeignKey(Commune, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

    def description_snippet(self):
        return self.description[:50] + '...'

    @staticmethod
    def get_chore(id):
        return Chore.objects.filter(id=id).first()

    def execute_chore(self, chore_id, user_id):
        chore = Chore.objects.filter(id=chore_id)[0]
        if (chore.passed is True and chore.assign_to == user_id):
            chore.completed = True
