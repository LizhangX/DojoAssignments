from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Username(models.Model):
    """Model definition for Username."""

    # TODO: Define fields here
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    