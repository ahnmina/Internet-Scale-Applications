from django.shortcuts import render
from django.http import HttpResponse
from django import template
from django.template.loader import get_template
import datetime

#from .models import Question

# # Create your views here.
# def index(request):
#     return HttpResponse("Hello, world. You're at the project1Homepage index.")
   
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('project1Homepage/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def current_datetime(request):
    now = datetime.datetime.now()
    return render(request, 'current_datetime.html', {'current_date': now})

def homepage(request):
	return render(request, 'homepage.html')