from django.shortcuts import render
from Dreioapp.forms import Studentform

def home(request):
    stud=Studentform
    return render(request,template_name='index.html',context={'form':stud})
