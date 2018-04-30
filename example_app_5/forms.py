"""
Form views for Example App 5.
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
            'price',
            'toppings',
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
    def __init__(self, *args, **kwargs):
        super(PizzaForm, self).__init__(*args, **kwargs)
        self.fields['toppings'].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields['toppings'].queryset = models.Topping.objects.all()

    class Meta:
        model = models.Pizza
        fields = {
            'name',
            'toppings',
        }

#endregion Standard Form Views
