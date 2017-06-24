from __future__ import unicode_literals

from django.db import models
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# Create your models here.
class UserManager(models.Manager):
    def register(self, form_data):
        errors = []
        if len(form_data['fname']) < 2 or not form_data['fname'].isalpha():
            errors.append('First name: No fewer than 2 characters; letters only')
        if len(form_data['lname']) < 2 or not form_data['fname'].isalpha():
            errors.append('Last name: No fewer than 2 characters; letters only')
        if len(form_data['email']) == 0 or not EMAIL_REGEX.match(form_data['email']):
            errors.append('Email: Please enter valid email!')
        if len(form_data['password']) < 8:
            errors.append('Password: Required; No fewer than 8 characters in length.')
        if form_data['confirm_pw'] != form_data['password']:
            errors.append('Password does not match pass word confirmation.')
        return errors

    def login(self, form_data):
        errors = []
        if len(form_data['log_email']) == 0 or not EMAIL_REGEX.match(form_data['log_email']):
            errors.append('Email: Please enter valid email!')
        if len(form_data['log_pw']) < 8:
            errors.append('Password: Required; No fewer than 8 characters in length.')
        if errors != []:
            return errors
        user = User.objects.filter(email=form_data['log_email']).first()
        if not user:
            errors.append('no username')
        else:
            if form_data['log_pw'] == user.password:
                return user
            errors.append('Invalid password!')
        return errors


    
class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        display = "first_name: {}, last_name: {}, email = {}".format(self.first_name, self.last_name, self.email)
        return display
    
    objects = UserManager()