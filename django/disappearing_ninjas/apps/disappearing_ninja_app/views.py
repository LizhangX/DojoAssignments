from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'disappearing_ninja_app/index.html')

def ninjas(request):
    return render(request,'disappearing_ninja_app/ninjas.html')

def color(request,ninja_color):
    if ninja_color == 'blue':
        image = 'leonardo.jpg'
    elif ninja_color == 'orange':
        image = 'michelangelo.jpg'
    elif ninja_color == 'red':
        image = 'raphael.jpg'
    elif ninja_color == 'purple':
        image = 'donatello.jpg'
    else:
        image = 'notapril.jpg'
    context = {
            'image': 'disappearing_ninja_app/img/' + image,
        }
    return render(request, 'disappearing_ninja_app/display_color.html', context)