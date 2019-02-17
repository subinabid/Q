from django.db import models

class quizid(models.Model)
    quiz_id = models.IntegerField()
    quiz_date = models.DateTimeField()

class question(models.Model):
    quiz_id = models.ForeignKey(quiz_id, on_delete = models.CASCADE)
    question_id = models.IntegerField()
    question_text = models.TextField()
    question_ans = models.TextField()
    has_options = models.CharField(max_length=2)
    has_media = models.CharField(max_length=200)

class answers(models.Model):
    quiz_id = models.IntegerField()
    question_id = models.IntegerField()
    user = models.CharField(max_length=10)
    answer = models.CharField(max_length = 200)
    ans_date = models.DateTimeField(auto_now = True, blank = True)

class attempt(models.Model):
    quiz_id = models.IntegerField()
    user = models.CharField(max_length = 10)
    login_date = models.DateTimeField(auto_now = True, blank = True)
