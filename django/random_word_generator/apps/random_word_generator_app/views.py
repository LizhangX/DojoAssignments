from django.shortcuts import render, redirect
import random
import string

# Create your views here.
def index(request):
    # request.session['random_word'] = ''
    # request.session['count'] = 0
    if 'count' not in request.session:
        request.session['count'] = 0
    if 'random_word' not in request.session:
        request.session['random_word'] = ''
    return render(request, 'random_word_generator_app/index.html')

def count(request):
    request.session['random_word'] = ''.join(random.choice(string.ascii_uppercase + string.digits) for i in range(14))
    request.session['count'] += 1
    return redirect('/')