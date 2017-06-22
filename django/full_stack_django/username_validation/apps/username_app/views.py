from django.shortcuts import render, redirect
from .models import Username
# Create your views here.
def index(request):
    if 'error' not in request.session:
        request.session['error'] = 0
    return render(request, 'username_app/index.html')

def success(request):
    print Username.objects.all()
    context = {
        'usernames': Username.objects.all()
    }
    return render(request, 'username_app/success.html', context)

def process(request):
    if request.method == "POST":
        if len(request.POST['name']) > 8 and len(request.POST['name']) < 26:
            Username.objects.create(name=request.POST['name'])
            request.session['error'] = 0
            return redirect('/success')
        else:
            request.session['error'] = 1
            return redirect('/')
    