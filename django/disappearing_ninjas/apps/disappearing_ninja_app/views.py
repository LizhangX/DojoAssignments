from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'disappearing_ninja_app/index.html')

def ninjas(request):
    return render(request,'disappearing_ninja_app/ninjas.html')

def color(request,ninja_color):
    
        
    return render(request, 'disappearing_ninja_app/display_color.html', context)