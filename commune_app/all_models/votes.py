from django.db import models
from .chores import Chore
from .users import User


class Poll(models.Model):
    chore = models.OneToOneField(Chore, on_delete=models.DO_NOTHING)
    question = models.TextField()
    option_one = models.CharField(max_length=30)
    option_two = models.CharField(max_length=30)
    option_one_count = models.IntegerField(default=0)
    option_two_count = models.IntegerField(default=0)

    @staticmethod
    def create_new_poll(chore_id):
        Poll(chore=chore_id, question=chore_id.title, option_one='Yes', option_two='No')

    def check_passage(self):
        # if self.option_one_count > self.option_two_count:
        #    self.chore.passed = True
        #    self.chore.save()
        self.chore.passed = True
        self.chore.save()

    def total(self):
        return self.option_one_count + self.option_two_count


class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chore = models.ForeignKey(Chore, on_delete=models.CASCADE)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, default=0)
    approve = models.BooleanField(default=False)

    # creates a new vote while checking if the related Chore can be passed or not
    @staticmethod
    def create_new_vote(voting_user, voted_chore, mypoll, vote_bool):
        Vote(user=voting_user, chore=voted_chore, poll=mypoll, approve=vote_bool).save()
        # temporarily compared the number of votes to 3 until we get a method in commune model
        # that returns the number of members in the commune
        if len(Vote.objects.filter(chore=voted_chore)) == 3:
            mypoll.check_passage()
