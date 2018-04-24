"""
Models for Example_App_1.
"""

from django.db import models


class Category(models.Model):
    # Standard model fields.
    title = models.CharField(max_length=200)
    # Auto-updating fields.
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
