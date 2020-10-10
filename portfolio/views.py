from django.shortcuts import render
from .models import Project

# Create your views here.


def home(request):
    projects_data = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects_data': projects_data})
