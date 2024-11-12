from django import forms
from .models import TaskCategoryModel

class Form(forms.ModelForm):
    class Meta:
        model=TaskCategoryModel
        fields='__all__'
        labels={'name':'Category Type:'}