from django.shortcuts import render, redirect
from django.http import HttpResponse
from todolist.models import Task
from todolist.forms import TaskForm

# Create your views here.
def home(request):
    context = {
        'page': 'Todo Manager'
    }
    return render(request, "home.html", context) 

def todolist(request):
    if request.method == "POST":
        form_data = TaskForm(request.POST or None)
        if form_data.is_valid():
            form_data.save()
            return redirect("todolist")
        
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
