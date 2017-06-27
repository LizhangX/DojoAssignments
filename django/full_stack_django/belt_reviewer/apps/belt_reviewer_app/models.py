from __future__ import unicode_literals

from django.db import models
import re
import bcrypt
# Create your models here.
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
class UserManager(models.Manager):
    def register(self, form_data):
        errors = []
        
        if len(form_data['fname']) == 0:
            errors.append('First name required.')
        if len(form_data['lname']) == 0:
            errors.append('Last name required.')
        if len(form_data['email']) == 0 or not EMAIL_REGEX.match(form_data['email']):
            errors.append('Email is invalid!')
        if len(form_data['password']) < 8:
            errors.append('Password must be at least 8 characters long.')
            return errors
        if form_data['password'] != form_data['confirm_pw']:
            errors.append('Password not matched.')
            return errors
        # is email unique
        duplicate = User.objects.filter(email=form_data['email'])
        print 'inside check unique'
        if duplicate:
            errors.append('This email has been used.')
        
        return errors

    def create_user(self, form_data):
        pw = str(form_data['password'])
        hashed_pw = bcrypt.hashpw(pw, bcrypt.gensalt())
        
        user = User.objects.create(
            first_name = form_data['fname'],
            last_name = form_data['lname'],
            email = form_data['email'],
            password = hashed_pw 
        )

        return user
        
    def login(self, form_data):
        errors = []
        if len(form_data['log_email']) == 0 or not EMAIL_REGEX.match(form_data['log_email']):
            errors.append('Log in email is invalid!')
        if len(form_data['log_pw']) < 8:
            errors.append('Password must be at least 8 characters long.')
        if errors != []:
            return errors
        user = User.objects.filter(email=form_data['log_email']).first()
        if user:
            pw = str(form_data['log_pw'])
            user_password = str(user.password)
            hashed_pw = bcrypt.hashpw(pw, user_password)
            if user_password == hashed_pw:
                return user
        errors.append('no matching email')
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

class Author(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, related_name="books")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Review(models.Model):
    review = models.CharField(max_length=50)
    rating = models.IntegerField()
    user = models.ForeignKey(User, related_name="reviews")
    book = models.ForeignKey(Book, related_name="reviewed")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
