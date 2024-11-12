from django.shortcuts import render
from task import models
def home(request):
    tasks=models.TaskModel.objects.all()
    for task in tasks:
         print(task.is_completed)
         for category1 in task.category.all():
              print(category1)
    return render(request,'home.html',{'tasks':tasks})