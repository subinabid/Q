from django.shortcuts import render
from django.http import HttpResponse
from .models import question, answers
from .forms import AnswerForm, OptionsForm

def quiz(request):
    return render(request, 'quiz/quiz.html',{})

def que(request, que_id):
    try:
        a = answers.objects.get(question_id = que_id, user = request.user.get_username())
    except:
        ans_text = ''
    else:
        ans_text = a.answer
    que_list = question.objects.filter(question_id = que_id )
    q = question.objects.get(question_id = que_id)
    has_options = q.has_options
    has_media = q.has_media
    form1 = OptionsForm()
    form2 = AnswerForm()
    context = {'que_list': que_list, 'que_id' : que_id,'has_options':has_options, 'has_media':has_media, 'form1' : form1, 'form2' : form2, 'range': range(20), 'answer':ans_text}
    return render(request, 'quiz/que.html', context)

def submit(request, que_id):

    try:
        a = answers.objects.get(question_id = que_id, user = request.user.get_username())  #check if the answer already exists
    except: #if answers doesnot exist, it will throw an exception. Save the submission to database
        p = answers(question_id = que_id, user = request.user.get_username(), answer = request.POST.get("answer") )
        p.save()
        ans_text = request.POST.get("answer") #pass the value from POST to template
    else: #if answer already exist, delete it and save the new value
        a.delete()
        p = answers(question_id = que_id, user = request.user.get_username(), answer = request.POST.get("answer") )
        p.save()
        ans_text = request.POST.get("answer") #pass the value from POST to template
    que_list = question.objects.filter(question_id = que_id )
    q = question.objects.get(question_id = que_id)
    has_options = q.has_options
    has_media = q.has_media
    form1 = OptionsForm()
    form2 = AnswerForm()
    context = {'que_list': que_list, 'que_id' : que_id,'has_options':has_options, 'has_media':has_media, 'form1' : form1, 'form2' : form2, 'range': range(20), 'answer':ans_text}
    return render(request, 'quiz/que.html', context)

def submission(request):
    subanswers = answers.objects.filter(user = request.user.get_username())
    context = {'subanswers': subanswers}
    return render(request,'quiz/submission.html', context)
