from django.shortcuts import render, HttpResponse, redirect
from apps.first_app.models import Course
from django.contrib import messages
from time import gmtime, localtime, strftime
from django.utils.crypto import get_random_string

# the index function is called when root is visited
def index(request):
    context = {
        "courses": Course.objects.all()        
    }
    return render(request, "first_app_templates/index.html", context)

def create(request):
    if request.method == "POST":
        Course.objects.create(name=request.POST["name"], desc=request.POST["desc"])
        return redirect('/')

def destroy(request, id):
    context = {
        "courses" : Course.objects.get(id=id)
    }
    return render(request, "first_app_templates/destroy.html", context)

def go_back(request):
    return redirect('/')

def delete(request, id):
    d = Course.objects.get(id=id)
    d.delete()
    return redirect('/')
