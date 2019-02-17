from django.contrib import admin
from .models import quizid, question, answers, attempt

class quizidadmin(admin.ModelAdmin):
    list_display = ('quiz_id', 'quiz_date')

class questionadmin(admin.ModelAdmin):
    list_display = ('quiz_id', 'question_id', 'question_text', 'question_ans', 'has_options', 'has_media')

class answersadmin(admin.ModelAdmin):
    list_display = ('quiz_id','user','question_id' , 'answer','ans_date')

class attemptadmin(admin.ModelAdmin):
    list_display = ('quiz_id', 'user', 'login_date')

admin.site.register(quizid, quizidadmin)
admin.site.register(question, questionadmin)
admin.site.register(answers, answersadmin)
admin.site.register(attempt, attemptadmin)
