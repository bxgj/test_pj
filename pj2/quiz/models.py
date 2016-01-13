from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.forms import ModelForm,TextInput,DateTimeInput

class Question(models.Model):
    question_text=models.CharField(max_length=20)
    pub_date=models.DateField(default=timezone.now())
    def __unicode__(self):
        return self.question_text          

class Choice(models.Model):
    choice_text=models.CharField(max_length=20)
    question=models.ForeignKey('Question',on_delete=models.CASCADE,)
    def __unicode__(self):
        return self.choice_text

class QuestionForm(ModelForm):
    class Meta:
        model=Question
        fields='__all__'
        widgets={
            'question_text':TextInput(attrs={'class':'form-control','placeholder':'question_text'}),
            'pub_date':DateTimeInput(attrs={'class':'form-control','type':'datetime'})            
        }
    
