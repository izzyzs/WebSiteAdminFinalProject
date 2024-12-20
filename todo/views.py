from django.shortcuts import render, redirect
from .models import Task

def home(request):
    tasks = Task.objects.all()
    return render(request, 'home.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        Task.objects.create(title=title, description=description)
        return redirect('/')
    return render(request, 'add_task.html')

def edit_task(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        maybe_title = request.POST.get('title') 
        maybe_description = request.POST.get('description')
        if maybe_title != "":
            task.title = maybe_title 
        if maybe_description != "":
            task.description = maybe_description
        task.completed = 'completed' in request.POST
        task.save()
        return redirect('/')
    return render(request, 'edit_task.html', {'task': task})

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('/')