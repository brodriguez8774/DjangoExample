"""
Forms for Example_App_8.
"""

from django import forms

from . import models


class CategoryForm(forms.ModelForm):
    """
    Form view for Category model.
    """
    class Meta:
        model = models.Category
        fields = {
            'title',
        }
