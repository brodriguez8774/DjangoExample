"""
Models for Example_App_2.
"""

from django.db import models
from django.urls import reverse


class Category(models.Model):
    # Model fields.
    title = models.CharField(max_length=200)
    # Self-setting/Non-user-editable fields.
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('example_app_2:category_detail', kwargs={'pk': self.pk})
