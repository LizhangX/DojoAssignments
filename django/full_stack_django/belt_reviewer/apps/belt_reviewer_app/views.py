from django.shortcuts import render, redirect, reverse
from .models import User, Author, Book, Review
from django.db.models import Count
from datetime import datetime
# Create your views here.
def index(request):
    print "Inside the index method."
    if 'errors' not in request.session:
        request.session['errors'] = []
    context ={
        'errors': request.session['errors'],
    }
    request.session.pop('errors')
    return render(request,'belt_reviewer_app/index.html',context)

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
        form_data = request.POST
        check = User.objects.login(form_data)
        if type(check) == type(User()):
            request.session['user_id'] = check.id
            return redirect(reverse('success'))
        request.session['errors'] = check
        return redirect(reverse('index'))
    return redirect(reverse('index'))
        
def logout(request):
    print "Inside the logout method."
    request.session.pop('user_id')
    return redirect(reverse('index'))

def success(request):
    print "Inside the success method."
    if 'user_id' in request.session:
        user_id = request.session['user_id']
        user = User.objects.get(id=user_id)

        recent_reviews = Review.objects.all().order_by('-created_at')[:3]
        recent_reviews_books = recent_reviews.values_list('book__id', flat=True)
        other_reviews = Book.objects.filter(reviewed__isnull=False).distinct().exclude(id__in=recent_reviews_books)
        
        context = {
            'recent_reviews': recent_reviews,
            'other_reviews': other_reviews,
            'current_user': user,
            'all_user': User.objects.all(),
        }
        return render(request, 'belt_reviewer_app/success.html', context)
    return redirect(reverse('index')) 

def display_add(request):
    authors = Author.objects.all()
    context = {
        "authors": authors,
    }
    return render(request,'belt_reviewer_app/add_book.html',context)
def add(request):
    print "Inside the add method."
    if request.method == "POST":
        form_data = request.POST
        user_id = request.session['user_id']
        if form_data['ex_author']:
            author = Author.objects.get(name = form_data['ex_author'])
        else:
            if Author.objects.filter(name = form_data['author']):
                author = Author.objects.get(name = form_data['author'])
            else:
                author = Author.objects.create(name = form_data['author'])
        user = User.objects.get(id=user_id)
        book = Book.objects.create(
            title = form_data['title'],
            author = author,
            )
        review = Review.objects.create(
            review = form_data['review'],
            rating = form_data['rating'],
            user = user,
            book = book,
        )
        return redirect(reverse('success'))
    return redirect(reverse('index')) 

def book(request, book_id):
    reviews = Review.objects.filter(book__id=book_id)
    book = Book.objects.get(id=book_id)
    current_user = User.objects.get(id=request.session['user_id'])
    context = {
        'reviews': reviews,
        'book': book,
        'current_user': current_user,
    }
    return render(request, "belt_reviewer_app/book.html", context)

def add_review(request, book_id):
    print 'Inside add_review method.'
    if request.method == "POST":
        form_data = request.POST
        user_id = request.session['user_id']
        current_user = User.objects.get(id=user_id)
        book = Book.objects.get(id = book_id)
        review = Review.objects.create(
            review = form_data['review'], 
            rating = form_data['rating'],
            user = current_user,
            book = book,
        )
        return redirect(reverse('book', kwargs={'book_id':book_id}))
    return redirect(reverse('index'))    

def delete_review(request, review_id):
    book_id = Review.objects.get(id=review_id).book.id
    Review.objects.get(id=review_id).delete()
    return redirect(reverse('book', kwargs={'book_id':book_id}))

def view_user(request, user_id):
    user = User.objects.get(id=user_id)
    books = Book.objects.filter(reviewed__user__id = user_id).distinct()
    context = {
        'user': user,
        'books': books,
    }
    return render(request, 'belt_reviewer_app/user.html', context)
