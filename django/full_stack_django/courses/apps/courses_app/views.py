from django.shortcuts import render, redirect
from .models import Course
# Create your views here.
def index(request):
    context = {
        'courses': Course.objects.all()
    }
    return render(request, 'courses_app/index.html', context)

def delete(request,id):    
    Course.objects.get(id=id).delete()
    return redirect('/')

def add(request):
    Course.objects.create(name=request.POST['name'],description=request.POST['description'])
    return redirect('/')

def confirm(request,id):
    print 'inside confirm'
    context = {
        'courses': Course.objects.get(id=id)
    }
    return render(request, 'courses_app/confirm.html', context)