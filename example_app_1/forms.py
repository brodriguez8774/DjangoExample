"""
Forms for Example App 1.
"""

from django import forms

from . import models


class CategoryForm(forms.ModelForm):
    """
    Define standard form view for Category model.
    """
    class Meta:
        model = models.Category
        fields = [
            'title',
        ]
