"""
Form views for Example App 4.
"""

from django import forms

from . import models


#region Admin Form Views

class ToppingAdminForm(forms.ModelForm):
    """
    Define admin form view for Topping model.
    """
    class Meta:
        model = models.Topping
        fields = {
            'name',
        }


class PizzaAdminForm(forms.ModelForm):
    """
    Define admin form view for Pizza model.
    """
    class Meta:
        model = models.Pizza
        fields = {
            'name',
            'toppings',
            'price',
        }

#endregion Admin Form Views


#region Standard Form Views

class ToppingForm(forms.ModelForm):
    """
    Define admin form view for Topping model.
    """
    class Meta:
        model = models.Topping
        fields = {
            'name',
        }


class PizzaForm(forms.ModelForm):
    """
    Define admin form view for Pizza model.
    """
    class Meta:
        model = models.Pizza
        fields = {
            'name',
            'toppings',
            'price',
        }

#endregion Standard Form Views
