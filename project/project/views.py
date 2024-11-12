from django.shortcuts import render
from task import models
def home(request):
    tasks=models.TaskModel.objects.all()

    for task in tasks:
         print(task.is_completed)
    return render(request,'home.html',{'tasks':tasks})