from django.shortcuts import render, redirect
import random
# Create your views here.
images = ['snow.jpg','desert.jpg','forest.jpg','vineyard.jpg','tropical.jpg']
def index(request):
    return render(request, 'landscapes_app/index.html')

def is_prime(x):
    if x > 1:
        n = x // 2
        for i in range(2, n + 1):
            if x % i == 0:
                return False
        return True
    else:
        return False

def show(request,number):
    show_msg = ''
    
    num = int(number)
    if is_prime(num) == True:
        show_msg = images[random.randint(0,4)]
    elif num in range(1,11):
        show_msg = images[0]
    elif num in range(11,21):
        show_msg = images[1]
    elif num in range(21,31):
        show_msg = images[2]
    elif num in range(31,41):
        show_msg = images[3]
    elif num in range(41,51):
        show_msg = images[4]
    context = {
        'msg': 'landscapes_app/img/' + show_msg,
    }
    return render(request, 'landscapes_app/show.html', context)

