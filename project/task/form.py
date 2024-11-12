from django import forms
from .models import TaskModel

class Form(forms.ModelForm):
    class Meta:
        model=TaskModel
        fields='__all__'