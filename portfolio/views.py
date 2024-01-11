from django.shortcuts import render
from django.http import HttpResponse
from .models import Project, AboutData

def index(request):
    data = AboutData.objects.latest('syntax')
    project = Project.objects.all()
    return render(request, "index.html", {'data':data, "project":project})

