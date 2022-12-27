from django.db import models
from sqlalchemy import false, true
from . import Chore
from . import users
from . import Commune


class Vote(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chore = models.ForeignKey(Chore, on_delete=models.CASCADE)
    approve = models.BooleanField()

    # creates a new vote while checking if the related Chore can be passed or not
    @staticmethod
    def create_new_vote(Vid, VotingUser, VotedChore, VoteBool):
        Vote(Vid, VotingUser, VotedChore, VoteBool).save()
        if len(Vote.filter(chore=VotingUser)) == len(Commune.members):
            num_of_yes_votes = Vote.filter(chore=VotedChore, approve=true)
            num_of_no_votes = Vote.filter(chore=VotedChore, approve=false)
            if num_of_yes_votes > num_of_no_votes:
                chore = Chore.get_chore(VotedChore)
                chore.passed = true
