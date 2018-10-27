from django.shortcuts import render
from django.http import HttpResponse
from .models import question

def quiz(request):
    return render(request, 'quiz/quiz.html',{})

def que(request, que_id):
    que_list = question.objects.filter(question_id = que_id )
    has_options = question.objects.only('has_options').filter(question_id = que_id)
    has_media = question.objects.only('has_media').filter(question_id = que_id)
    context = {'que_list': que_list, 'que_id' : que_id,'has_options':has_options, 'has_media':has_media}
    return render(request, 'quiz/que.html', context)
