"""
Views for Example App 3.
"""

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from . import forms, models


def index(request):
    """
    Index view.
    """
    # Send to template for user display.
    return render(request, 'example_app_3/index.html')


#region Overview Views

def address_overview(request):
    """
    List view for Address model.
    """
    # Pull models from database.
    address_list = models.Address.objects.all()

    # Send to template for user display.
    return render(request, 'example_app_3/address_overview.html', {
        'address_list': address_list,
    })


def customer_overview(request):
    """
    List view for Customer model.
    """
    # Pull models from database.
    customer_list = models.Customer.objects.all()

    # Send to template for user display.
    return render(request, 'example_app_3/customer_overview.html', {
        'customer_list': customer_list,
    })

#endregion Overview Views


#region Detail Views

def address_detail(request, pk):
    """
    Displays details of the given address.
    """
    # Pull models from database.
    address = get_object_or_404(models.Address, pk=pk)

    # Send to template for user display.
    return render(request, 'example_app_3/address_detail.html', {
        'address': address,
    })


def customer_detail(request, pk):
    """
    Displays details of the given customer.
    """
    # Pull models from database.
    customer = get_object_or_404(models.Customer, pk=pk)

    # Send to template for user display.
    return render(request, 'example_app_3/customer_detail.html', {
        'customer': customer,
    })

#endregion Detail Views


#region Create Views

def address_create(request):
    """
    Form view for creating a new Address.
    """
    form = forms.AddressForm()

    # Check if request is post.
    if request.method == 'POST':
        form = forms.AddressForm(request.POST)
        if form.is_valid():
            address = form.save()

            # Render response for user.
            return HttpResponseRedirect(reverse('example_app_3:address_detail', args=(address.pk, )))

    # Handle for non-post request.
    return render(request, 'example_app_3/forms/address.html', {
        'form': form,
    })


def customer_create(request):
    """
    Form view for creating a new Customer.
    """
    form = forms.CustomerForm()

    # Check if request is post.
    if request.method == 'POST':
        form = forms.CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save()

            # Render response for user.
            return HttpResponseRedirect(reverse('example_app_3:customer_detail', args=(customer.pk, )))

    # Handle for non-post request.
    return render(request, 'example_app_3/forms/customer.html', {
        'form': form,
    })

#endregion Create Views


#region Edit Views

def address_edit(request, pk):
    """
    Form view for editing a Address.
    """
    # Pull models from database.
    address = get_object_or_404(models.Address, pk=pk)
    form = forms.AddressForm(instance=address)

    # Check if request is post.
    if request.method == 'POST':
        form = forms.AddressForm(instance=address, data=request.POST)
        if form.is_valid():
            form.save()

            # Render response for user.
            return HttpResponseRedirect(reverse('example_app_3:address_detail', args=(address.pk, )))

    # Send to template for user display.
    return render(request, 'example_app_3/forms/address.html', {
        'form': form,
        'address': address,
    })


def customer_edit(request, pk):
    """
    Form view for editing a Customer.
    """
    # Pull models from database.
    customer = get_object_or_404(models.Customer, pk=pk)
    form = forms.CustomerForm(instance=customer)

    # Check if request is post.
    if request.method == 'POST':
        form = forms.CustomerForm(instance=customer, data=request.POST)
        if form.is_valid():
            form.save()

            # Render response for user.
            return HttpResponseRedirect(reverse('example_app_3:customer_detail', args=(customer.pk, )))

    # Send to template for user display.
    return render(request, 'example_app_3/forms/customer.html', {
        'form': form,
        'customer': customer,
    })

#endregion Edit Views
