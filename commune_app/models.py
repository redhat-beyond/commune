from django.db import models


class Decision(models.Model):
    EXPENSE = 'EX'
    CHORE = 'CH'
    DECISION_TYPE = [
        (EXPENSE, 'Expense'),
        (CHORE, 'Chore'),
    ]
    decision_type = models.CharField(max_length=2, choices=DECISION_TYPE)
    is_passed = models.BooleanField()
    title = models.CharField(max_length=127)
    recur = models.BooleanField()
    recur_freq = models.DateTimeField()
    time_range = models.DurationField()
