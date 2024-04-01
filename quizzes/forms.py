from django.forms import ModelForm
from django import forms
from .models import *
class QuizForm(ModelForm):
    class Meta:
        model = Quiz
        fields = ['name']
        labels = {
            'name': 'Название теста',
            
            }

        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }
    def __init__(self, *args, **kwargs):
        super(QuizForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control input-box form-ensurance-header-control'})    
class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['name']
        labels = {
            'name': 'Название вопроса',
            
            }

        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }
    def __init__(self, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control input-box form-ensurance-header-control'})    
