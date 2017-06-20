from __future__ import unicode_literals

from django.db import models

# Create your models here.
# A product should have a name, description, weight, price, cost (to seller), and category. Figure out what type should be assigned to each field.

# Once all the previous steps are complete, test your code by adding 3 new products. Retrieve all rows from your table and print each to the console.
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=1000)
    weight = models.FloatField(max_length=45)
    price = models.FloatField(max_length=45)
    cost = models.FloatField(max_length=45)
    category = models.CharField(max_length=255)
    
