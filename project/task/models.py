from django.db import models
from category.models import TaskCategoryModel

class TaskModel(models.Model):
    taskTitle =models.CharField(max_length=40)
    taskDescription=models.TextField()
    is_completed=models.BooleanField()
    category=models.ManyToManyField(TaskCategoryModel)
    def __str__(self):
        return self.taskTitle