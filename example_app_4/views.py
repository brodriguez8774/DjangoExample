"""
Views for Example App 4.
"""

from django.http import HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from . import forms, models


def index(request):
    """
    Index view.
    """
    # Send to template for user display.
    return render(request, 'example_app_4/index.html')


#region Overview Views

def topping_overview(request):
    """
    List view for Topping model.
    """
    # Pull models from database.
    topping_list = models.Topping.objects.all()

    # Send to template for user display.
    return render(request, 'example_app_4/topping_overview.html', {
        'topping_list': topping_list,
    })


def pizza_overview(request):
    """
    List view for Pizza model.
    """
    # Pull models from database.
    pizza_list = models.Pizza.objects.all()

    # Send to template for user display.
    return render(request, 'example_app_4/pizza_overview.html', {
        'pizza_list': pizza_list,
    })

#endregion Overview Views


#region Detail Views

def topping_detail(request, pk):
    """
    Displays details of the given Topping.
    """
    # Pull models from database.
    topping = get_object_or_404(models.Topping, pk=pk)

    # Send to template for user display.
    return render(request, 'example_app_4/topping_detail.html', {
        'topping': topping,
    })


def pizza_detail(request, pk):
    pizza = get_object_or_404(models.Pizza, pk=pk)
    topping_set = pizza.toppings.all()

    return render(request, 'example_app_4/pizza_detail.html', {
        'pizza': pizza,
        'topping_set': topping_set,
    })

#endregion Detail Views


#region Create Views

def topping_create(request):
    """
    Form view for creating a new Topping.
    """
    form = forms.ToppingForm()

    # Check if request is post.
    if request.method == 'POST':
        form = forms.ToppingForm(request.POST)
        if form.is_valid():
            topping = form.save()

            # Render response for user.
            return HttpResponseRedirect(reverse('example_app_4:topping_detail', args=(topping.pk, )))

    # Handle for non-post request.
    return render(request, 'example_app_4/forms/topping.html', {
        'form': form,
    })


def pizza_create(request):
    """
    Form view for creating a new Pizza.
    """
    form = forms.PizzaForm()

    # Check if request is post.
    if request.method == 'POST':
        form = forms.PizzaForm(request.POST)
        if form.is_valid():
            pizza = form.save()

            # Render response for user.
            return HttpResponseRedirect(reverse('example_app_4:pizza_detail', args=(pizza.pk, )))

    # Handle for non-post request.
    return render(request, 'example_app_4/forms/pizza.html', {
        'form': form,
    })

#endregion Create Views


#region Edit Views

def topping_edit(request, pk):
    """
    Form view for editing a Topping.
    """
    # Pull models from database.
    topping = get_object_or_404(models.Topping, pk=pk)
    form = forms.ToppingForm(instance=topping)

    # Check if request is post.
    if request.method == 'POST':
        form = forms.ToppingForm(instance=topping, data=request.POST)
        if form.is_valid():
            form.save()

            # Render response for user.
            return HttpResponseRedirect(reverse('example_app_4:topping_detail', args=(topping.pk, )))

    # Send to template for user display.
    return render(request, 'example_app_4/forms/topping.html', {
        'form': form,
        'topping': topping,
    })


def pizza_edit(request, pk):
    """
    Form view for editing a Pizza.
    """
    # Pull models from database.
    pizza = get_object_or_404(models.Pizza, pk=pk)
    form = forms.PizzaForm(instance=pizza)

    # Check if request is post.
    if request.method == 'POST':
        form = forms.PizzaForm(instance=pizza, data=request.POST)
        if form.is_valid():
            form.save()

            # Render response for user.
            return HttpResponseRedirect(reverse('example_app_4:pizza_detail', args=(pizza.pk, )))

    # Send to template for user display.
    return render(request, 'example_app_4/forms/pizza.html', {
        'form': form,
        'pizza': pizza,
    })

#endregion Edit Views
