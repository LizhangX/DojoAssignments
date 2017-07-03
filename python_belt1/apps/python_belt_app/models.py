from __future__ import unicode_literals

from django.db import models
import bcrypt
from datetime import datetime
# Create your models here.
class UserManager(models.Manager):
    def register(self, form_data):
        errors = []
        if len(form_data['name']) < 3:
            errors.append('Name must have at least 3 characters.')
        if len(form_data['username']) < 3:
            errors.append('Username must have at least 3 characters.')
        if len(form_data['password']) < 8:
            errors.append('Password must be at least 8 characters long.')
            return errors
        if form_data['password'] != form_data['confirm_pw']:
            errors.append('Password not matched.')
            return errors
        duplicate_username = User.objects.filter(username=form_data['username'])
        print 'checking unique'
        if duplicate_username:
            errors.append('This username has been used.')
        return errors

    def create_user(self, form_data):
        pw = str(form_data['password'])
        hashed_pw = bcrypt.hashpw(pw, bcrypt.gensalt())
        
        user = User.objects.create(
            name = form_data['name'],
            username = form_data['username'],
            password = hashed_pw 
        )
        return user
        
    def login(self, form_data):
        errors = []
        if len(form_data['log_username']) == 0:
            errors.append('Username is invalid!')
        if len(form_data['log_pw']) < 8:
            errors.append('Password must be at least 8 characters long.')
        if errors != []:
            return errors
        user = User.objects.filter(username=form_data['log_username']).first()
        if user:
            pw = str(form_data['log_pw'])
            user_password = str(user.password)
            hashed_pw = bcrypt.hashpw(pw, user_password)
            if user_password == hashed_pw:
                return user
        errors.append('invalid login')
        return errors

class User(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

class PlanManager(models.Manager):
    
    def validate(self, form_data):
        errors = []
        print datetime.now().date()
        print form_data['date_from']
        if len(form_data['destination']) == 0:
            errors.append('Destination is empty!')
        if len(form_data['description']) == 0:
            errors.append('Description is empty!')
        if not form_data['date_from']:
            errors.append('Travel Date From is empty!')
        if not form_data['date_to']:
            errors.append('Travel Date To is empty!')
            return errors
        if str(form_data['date_from']) < str(datetime.now().date()):
            errors.append('Travel dates should be future-dated!')
        if str(form_data['date_to']) < str(form_data['date_from']):
            errors.append('Travel Date To should not be before Travel Date From')            
        return errors

    def create_plan(self, form_data, current_user):
        plan = Plan.objects.create(
            destination = form_data['destination'],
            description = form_data['description'],
            date_from = form_data['date_from'],
            date_to = form_data['date_to'],
            created_by = current_user,
        )
        return plan

class Plan(models.Model):
    destination = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    date_from = models.DateField()
    date_to = models.DateField()
    created_by = models.ForeignKey(User, related_name='creates')
    joined_by = models.ManyToManyField(User, related_name='joins')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = PlanManager()
    