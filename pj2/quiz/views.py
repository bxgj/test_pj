from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from quiz.models import Question
from quiz.models import QuestionForm

def detail(request,qid):
    res="detail page of %s " % qid
    #myq=Question.objects.get(pk=qid)
    qf=QuestionForm()
    context={"res":res,"qf":qf}
    return render(request,'quiz/detail.html',context)

class QuestionList(ListView):
    model=Question
    context_object_name='question_list'
    template_name='quiz/index.html'
