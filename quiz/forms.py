from django import forms

class AnswerForm(forms.Form):
    answer = forms.CharField(label='Your Answer', max_length=100)
    answer2 = forms.CharField(max_length=100)
