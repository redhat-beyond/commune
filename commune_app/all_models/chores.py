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

    def execute_chore(self, user_id):
        if not self.passed:
            raise Exception("chore not passed")
        if self.assign_to_id is not user_id:
            raise Exception("this chore not assign to this user")
        if self.completed:
            raise Exception("chore already completed")
        self.completed = True
        self.save()
