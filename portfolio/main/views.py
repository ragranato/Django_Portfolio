from django.shortcuts import render, get_object_or_404
from .models import Project, Tag

# Create your views here.
def home(request):
    return render(request, "home.html")

def contact(request):
    projects = Project.objects.all()
    tags = Tag.objects.all()
    return render(request, "contact.html", {"projects":projects, "tags": tags})

def project(request, id):
    return render(request, "project.html")