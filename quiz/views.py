from django.shortcuts import render
from django.http import HttpResponse
from .models import question
from .forms import AnswerForm

def quiz(request):
    return render(request, 'quiz/quiz.html',{})

def que(request, que_id):
    que_list = question.objects.filter(question_id = que_id )
    q= question.objects.get(pk = que_id)
    has_options = q.has_options
    has_media = q.has_media
    context = {'que_list': que_list, 'que_id' : que_id,'has_options':has_options, 'has_media':has_media}
    return render(request, 'quiz/que.html', context)
