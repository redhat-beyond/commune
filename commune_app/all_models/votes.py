from django.db import models
from django.contrib.auth import get_user_model


class Vote(models.Model):
    user = models.ForeignKey('commune_app.User', on_delete=models.CASCADE)
    chore = models.ForeignKey('commune_app.Chore', on_delete=models.CASCADE)
    approve = models.BooleanField(default=False)

    # creates a new vote while checking if the related Chore can be passed or not
    @staticmethod
    def create_new_vote(voting_user, voted_chore, vote_bool):
        user_num = len(get_user_model().objects.filter(commune_id=voting_user.commune_id.id))
        user_vote = Vote(user=voting_user, chore=voted_chore, approve=vote_bool)
        user_vote.save()
        if len(Vote.objects.filter(chore=voted_chore)) == user_num:
            num_of_yes_votes = len(Vote.objects.filter(chore=voted_chore, approve=True))
            num_of_no_votes = len(Vote.objects.filter(chore=voted_chore, approve=False))
            if num_of_yes_votes > num_of_no_votes:
                voted_chore.passed = True
                voted_chore.save()

    def vote(self, chore_id, decision):
        Vote.create_new_vote(voting_user=self.id, voted_chore=chore_id, vote_bool=decision)


