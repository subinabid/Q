from django import forms

class AnswerForm(forms.Form):
    answer = forms.CharField(label='Your Answer', max_length=100)


class OptionsForm(forms.Form):
    CHOICES=[('select1','select 1'),
             ('select2','select 2')]
    options = forms.ChoiceField(label='Select Your Answer', choices=CHOICES,  widget = forms.RadioSelect)
