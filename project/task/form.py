from django import forms
from .models import TaskModel

class Form(forms.ModelForm):
    class Meta:
        model=TaskModel
        fields='__all__'
        labels={
            'taskTitle':'Task Name',
            'taskDescription':'Task Description',
            'is_completed':'Is Completed?',
            'category':'Task category'
        }