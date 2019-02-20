from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import logout
from .models import quizid, question, answers, attempt
from .forms import AnswerForm, OptionsForm

#Get the quiz_id
quiz_id_var = 1
################################################################################

# View for quiz home page
def quiz(request):
    try: #check if the user has logged in before
        l = attempt.objects.get(user = request.user.get_username(), quiz_id = quiz_id_var)
    except: #the user has not logged in before
        previous_attempt = 0
        if not request.user.is_staff:
            la = attempt(quiz_id = quiz_id_var, user = request.user.get_username())
            la.save()
    else: #the user has logged in before
        previous_attempt = 1
        logout(request)
    context = {'quiz_id': quiz_id_var, 'previous_attempt' : previous_attempt}
    return render(request, 'quiz/quiz.html', context)
################################################################################


# View for displaying questions
def que(request, que_id):
    try: # checking if the question is already answered
        a = answers.objects.get(quiz_id = quiz_id_var, question_id = que_id, user = request.user.get_username())
    except: # if there is no entry, python will trrow an error, then set answer to blank
        ans_text = ''
    else: # if no error is thrown, that indicates that an answer exists in the db
        ans_text = a.answer
    que_list = question.objects.filter(question_id = que_id )
    q = question.objects.get(question_id = que_id)
    has_options = q.has_options
    has_media = q.has_media
    form1 = OptionsForm()
    form2 = AnswerForm()
    context = {'quiz_id': quiz_id_var,'que_list': que_list, 'que_id' : que_id,'has_options':has_options, 'has_media':has_media, 'form1' : form1, 'form2' : form2, 'range': range(20), 'answer':ans_text}
    return render(request, 'quiz/que.html', context)
################################################################################


# View for submiting answers
def submit(request, que_id):
    try:
        a = answers.objects.get(quiz_id = quiz_id_var, question_id = que_id, user = request.user.get_username())   # checking if the question is already answered
    except: #if answers doesnot exist, it will throw an exception. Save the submission to database
        p = answers(quiz_id = quiz_id_var, question_id = que_id, user = request.user.get_username(), answer = request.POST.get("answer") )
        p.save()
        ans_text = request.POST.get("answer") #pass the value from POST to template
    else: #if answer already exist, delete it and save the new value
        a.delete()
        p = answers(quiz_id = quiz_id_var, question_id = que_id, user = request.user.get_username(), answer = request.POST.get("answer") )
        p.save()
        ans_text = request.POST.get("answer") #pass the value from POST to template
    que_list = question.objects.filter(question_id = que_id )
    q = question.objects.get(question_id = que_id)
    has_options = q.has_options
    has_media = q.has_media
    form1 = OptionsForm()
    form2 = AnswerForm()
    context = {'quiz_id': quiz_id_var, 'que_list': que_list, 'que_id' : que_id,'has_options':has_options, 'has_media':has_media, 'form1' : form1, 'form2' : form2, 'range': range(20), 'answer':ans_text}
    return render(request, 'quiz/que.html', context)
################################################################################


# View for final page
def submission(request):
    subanswers = answers.objects.filter(user = request.user.get_username()).order_by('question_id')
    context = {'subanswers': subanswers}
    return render(request,'quiz/submission.html', context)
################################################################################
