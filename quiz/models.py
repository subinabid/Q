from django.db import models

class question(models.Model):
    question_id = models.IntegerField()
    question_text = models.TextField()
    has_options = models.CharField(max_length=2)
    has_media = models.CharField(max_length=200)

class answers(models.Model):
    question_id = models.IntegerField()
    user = models.CharField(max_length=10)
    answer = models.CharField(max_length = 200)
