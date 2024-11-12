from django.shortcuts import render,redirect
from .form import Form
# Create your views here.

def addCategory(request):
    if request.method=='POST':
        form1=Form(request.POST)
        if form1.is_valid:
            form1.save()
            return redirect('showTasks')
            #return render(request,'addToCategory.html',{'form':form1})
    return render(request,'addToCategory.html',{'form':Form()})


