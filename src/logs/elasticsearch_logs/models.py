from django.db import models

from logs.utils import TimeStampMixin


class Logs(TimeStampMixin):
    client_id = models.CharField(max_length=100)
    query_id = models.CharField(max_length=100)
    question = models.TextField()
    question_matched = models.TextField()
    answer = models.TextField()
    action = models.CharField(max_length=100,blank=True,null=True)
    action_param = models.TextField(blank=True,null=True)
    score = models.FloatField()

    def __str__(self):
        return self.client_id