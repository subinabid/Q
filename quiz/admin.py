from django.contrib import admin
from .models import question, answers, attempt

class questionadmin(admin.ModelAdmin):
    list_display = ('question_id', 'question_text', 'question_ans', 'has_options', 'has_media')

class answersadmin(admin.ModelAdmin):
    list_display = ('user','question_id' , 'answer','ans_date')

class attemptadmin(admin.ModelAdmin):
    list_display = ('user', 'login_date')

admin.site.register(question, questionadmin)
admin.site.register(answers, answersadmin)
admin.site.register(attempt, attemptadmin)
