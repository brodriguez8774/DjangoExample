"""
Models for Example_App_7.
"""

from django.db import models
from django.urls import reverse


class Category(models.Model):
    # Model fields.
    title = models.CharField(max_length=200)
    ## Self-setting/Non-user-editable fields.
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return '{0}'.format(self.title)

    def get_absolute_url(self):
        return reverse('example_app_7:category_edit', kwargs={
            'pk': self.pk,
        })

    def save(self, *args, **kwargs):
        """
        Modify model save behavior.
        """
        # Save model.
        self.full_clean()
        super(Category, self).save(*args, **kwargs)


