from django.shortcuts import render
from django.http import HttpResponse
from todolist.models import Task

# Create your views here.
def home(request):
    context = {
        'page': 'Todo Manager'
    }
    return render(request, "home.html", context) 

def todolist(request):
    all_tasks = Task.objects.all()
    context = {
        'page': 'Todo List',
        'all_tasks': all_tasks
    }
    return render(request, "todolist.html", context) 

def contact(request):
    context = {
        'page': 'Contact Us'
    }
    return render(request, "contact.html", context) 

def about(request):
    context = {
        'page': 'About Us'
    }
    return render(request, "about.html", context) 
