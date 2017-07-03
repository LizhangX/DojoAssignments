from django.shortcuts import render, redirect, reverse
from .models import User, Plan
# Create your views here.

def index(request):
    print "Inside the index method."

    if 'errors' not in request.session:
        request.session['errors'] = []
    context ={
        'errors': request.session['errors'],
    }
    request.session.pop('errors')
    return render(request, 'python_belt_app/index.html', context)

def register(request):
    print "Inside the register method."

    if request.method == "POST":
        check = User.objects.register(request.POST)
        if not check:
            user = User.objects.create_user(request.POST)
            request.session['user_id'] = user.id
            return redirect(reverse('success'))
        request.session['errors'] = check
    return redirect(reverse('index'))
    
def login(request):
    print "Inside the login method."

    if request.method == "POST":
        check = User.objects.login(request.POST)
        if type(check) == type(User()):
            request.session['user_id'] = check.id
            return redirect(reverse('success'))
        request.session['errors'] = check
    return redirect(reverse('index'))
        
def logout(request):
    print "Inside the logout method."
    request.session.pop('user_id')
    return redirect(reverse('index'))

def success(request):
    user_id = request.session['user_id']
    current_user = User.objects.get(id =user_id)
    created_plan = Plan.objects.filter(created_by__id = user_id).order_by('id')
    joined_plan = Plan.objects.filter(joined_by__id = user_id)
    not_joined_plan = Plan.objects.exclude(joined_by__id = user_id).exclude(created_by__id=user_id)
    context = {
        'current_user': current_user,
        'created_plan': created_plan,
        'joined_plan': joined_plan,
        'not_joined_plan': not_joined_plan,

    }
    return render(request, 'python_belt_app/success.html', context)

def destination(request, plan_id):
    plan = Plan.objects.get(id=plan_id)
    other_users = User.objects.filter(joins__id=plan_id)
    context = {
        'plan': plan,
        'other_users': other_users,
    }
    return render(request,'python_belt_app/destination.html', context)

def join(request, plan_id):
    user_id = request.session['user_id']
    current_user = User.objects.get(id =user_id)
    plan = Plan.objects.get(id = plan_id)
    plan.joined_by.add(current_user)
    return redirect(reverse('success'))
    

def display_add(request):
    if 'plan_errors' not in request.session:
        request.session['plan_errors'] = []
    context = {
        'plan_errors': request.session['plan_errors'],
    }
    request.session.pop('plan_errors')
    return render(request,'python_belt_app/add_trip.html', context)

def add_plan(request):
    if request.method == "POST":
        user_id = request.session['user_id']
        current_user = User.objects.get(id =user_id)
        check = Plan.objects.validate(request.POST)
        if not check:
            plan = Plan.objects.create_plan(request.POST, current_user)
            return redirect(reverse('success'))
        request.session['plan_errors'] = check
        return redirect(reverse('display_add'))
    return redirect(reverse('success'))