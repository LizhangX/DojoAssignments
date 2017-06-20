from django.shortcuts import render,redirect
import random
# Create your views here.
VALUES = ['lol','wow','cs-go','fallout4', 'GTA5','Need for Speed','NBA']
def index(request):
    if 'items' not in request.session:
        request.session['items'] = []
    return render(request, 'surprise_me_app/index.html')

def process(request):
    if request.method == 'POST':
        request.session['items'] = random.sample(VALUES,int(request.POST['number']))
    return redirect('/results')

def results(request):
    return render(request, 'surprise_me_app/results.html')