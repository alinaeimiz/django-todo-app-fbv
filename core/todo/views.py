from django.shortcuts import render,redirect
from .forms import TaskForms
from django.contrib import messages
from .models import Task
from django.contrib.auth.decorators import login_required
 # Create your views here.
@login_required
def todo_view(request):
    posts = Task.objects.filter(user = request.user)
    if request.method == 'POST':
        form = TaskForms(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            messages.success(request,'new task is active')
        else:
            messages.error(request,'new task is failed')
        return redirect('/')
        
    return render(request, 'to-do-list.html',{'posts' : posts},)



def delete_view(request,pk):
    posts = Task.objects.filter(user= request.user).get(id=pk)
    if request.method == 'GET':
        posts = posts.delete()
        messages.success(request, 'your task is deleted')
    return redirect('/')


def finished_view(request,pk):
    posts = Task.objects.filter(user= request.user)
    if request.method == 'GET':
        posts.filter(id=pk).update(completed=True)
        messages.success(request, 'your task is completed')
    return redirect('/')

