"""
Forms for Example App 3.
"""

from django import forms

from . import models


#region Admin Form Views

class AddressAdminForm(forms.ModelForm):
    """
    Define admin form view for Address model.
    """
    class Meta:
        model = models.Address
        # Define all fields which you wish to have displayed.
        # Note that this is not necessarily the order displayed. It just determines what is displayed at all.
        # Useful if you want hidden/automatically-updating fields to hold metadata within a model.
        fields = {
            'address',
        }
        # Define all custom error messages, such as example.
        # Note that Django should automatically create a error message for max_length.
        # This example overrides the default.
        error_messages = {
            'address': {
                'max_length': 'Field is too long. Must be less than 200 characters.'
            }
        }


class CustomerAdminForm(forms.ModelForm):
    """
    Define admin form view for Customer model.
    """
    class Meta:
        model = models.Customer
        fields = {
            'address',
            'first_name',
            'last_name',
        }
        # Change what a field is displayed as in the admin front end view.
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
        }


#endregion Admin Form Views



#region Standard Form Views

class AddressForm(forms.ModelForm):
    """
    Define standard form view for Address model.
    """
    class Meta:
        model = models.Address
        fields = {
            'address',
        }


class CustomerForm(forms.ModelForm):
    """
    Define standard form view for Customer model.
    """
    class Meta:
        model = models.Customer
        fields = {
            'address',
            'first_name',
            'last_name',
        }

#endregion Standard Form Views
