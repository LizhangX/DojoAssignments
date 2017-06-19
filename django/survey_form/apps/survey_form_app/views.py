from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    if 'context' not in request.session:
        request.session['context'] = {}
    if 'count' not in request.session:
        request.session['count'] = 0
    return render(request, 'survey_form_app/index.html')

def process(request):
    request.session['context'] = {
        'name': request.POST['name'],
        'location': request.POST['location'],
        'language': request.POST['language'],
        'comment': request.POST['comment'],
    }
    request.session['count'] += 1
    return redirect('/result')

def result(request):
    context = request.session['context']
    return render(request, 'survey_form_app/result.html', context)


# request.session['name'] = request.POST['name']
#     request.session['location'] = request.POST['location']
#     request.session['language'] = request.POST['language']
#     request.session['comment'] = request.POST['comment']
#     request.session['count'] += 1 