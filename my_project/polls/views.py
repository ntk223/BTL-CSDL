from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
def index(request):
    name = 'Django'
    taisan1 = ['laptop','smartphone','tablet']
    return render( request, 'polls/index.html' , {'name':name , 'taisan':taisan1})  

def viewlist(request):
    question_list = Question.objects.all()
    context = {'question_list': question_list}
    return render(request, 'polls/question_list.html', context)

def detailView(request, question_id):
    q = Question.objects.get(pk=question_id)
    return render(request, 'polls/detail_question.html', {'qs':q})

def vote(request, question_id):
    q = Question.objects.get(pk=question_id)
    try:
        dulieu = request.POST['choice']
        c = q.choice_set.get(pk=dulieu)
    except:
        HttpResponse("You didn't select a choice")
    c.votes += 1
    c.save()
    return render(request, 'polls/result.html', {'qs':q})

     

    