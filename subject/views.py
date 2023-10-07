from django.shortcuts import render
from .models import Subject
# Create your views here.
def mainPage(request):
    subjects_list = Subject.objects.all()
    return render(request,'subject.html',{"subjects_list":subjects_list})
