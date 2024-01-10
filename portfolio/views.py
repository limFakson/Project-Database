from django.shortcuts import render
from django.http import HttpResponse
from .models import Project, AboutData

def index(request):
    return render(request, "index.html")

def about(request):
    data = AboutData.objects.first()
    return render(request, "about.html", {'data':data})