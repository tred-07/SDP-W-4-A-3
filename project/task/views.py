from django.shortcuts import render,redirect
from .form import Form
from . import models
# Create your views here.

def addToTask(request):
    if request.method=='POST':
        form1=Form(request.POST)
        if form1.is_valid:
            form1.save()
            return redirect('showTasks')
    return render(request,'addToTask.html',{'form':Form()})

def editTask(request,id):
    task=models.TaskModel.objects.get(pk=id)
    form1=Form(instance=task)
    if request.method=='POST':
        form1=Form(request.POST,instance=task)
        if form1.is_valid:
            form1.save()
            return redirect('showTasks')
    return render(request,'editTask.html',{'form':form1})

def deleteTask(request,id):
    task=models.TaskModel.objects.get(pk=id)
    task.delete()
    return redirect('showTasks')

