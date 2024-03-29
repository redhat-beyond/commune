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

    @staticmethod
    def create_chore(title, description, budget, assign_to, commune_id, date):
        user = User.objects.get(id=assign_to)
        commune = Commune.objects.get(id=commune_id)
        chore = Chore(title=title, description=description, budget=budget, assign_to=user, commune_id=commune,
                      date=date, passed=False, completed=False)
        chore.save()
        return chore

    def description_snippet(self):
        return self.description[:50] + '...'

    @staticmethod
    def get_chore(id):
        return Chore.objects.filter(id=id).first()

    @staticmethod
    def execute_chore(chore_id, user_id):
        chore = Chore.objects.filter(id=chore_id).first()
        user = User.objects.filter(id=user_id).first()
        if chore.passed and chore.assign_to.id == user_id:
            chore = Chore.objects.filter(id=chore_id).first()
            chore.completed = True
            chore.save()
            commune = Commune.objects.filter(id=user.commune_id.id).first()
            commune.wallet_charge(chore.budget)
            commune.save()
        return chore.completed
