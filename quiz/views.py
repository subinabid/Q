from django.shortcuts import render
from django.http import HttpResponse
from .models import question, answers
from .forms import AnswerForm, OptionsForm

def quiz(request):
    return render(request, 'quiz/quiz.html',{})

def que(request, que_id):
    que_list = question.objects.filter(question_id = que_id )
    q = question.objects.get(pk = que_id)
    has_options = q.has_options
    has_media = q.has_media
    form1 = OptionsForm()
    form2 = AnswerForm()
    context = {'que_list': que_list, 'que_id' : que_id,'has_options':has_options, 'has_media':has_media, 'form1' : form1, 'form2' : form2}
    return render(request, 'quiz/que.html', context)

def submit(request, que_id):

    p = answers(question_id = que_id, user = request.user.get_username(), answer = request.POST.get("answer") )
    p.save()
    que_list = question.objects.filter(question_id = que_id )
    q = question.objects.get(pk = que_id)
    has_options = q.has_options
    has_media = q.has_media
    form1 = OptionsForm()
    form2 = AnswerForm()
    context = {'que_list': que_list, 'que_id' : que_id,'has_options':has_options, 'has_media':has_media, 'form1' : form1, 'form2' : form2}
    return render(request, 'quiz/que.html', context)
