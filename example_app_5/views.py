"""
Views for Example App 5.
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
    return render(request, 'example_app_5/index.html')


#region Overview Views

def topping_overview(request):
    """
    List view for Topping model.
    """
    # Pull models from database.
    topping_list = models.Topping.objects.all()

    # Send to template for user display.
    return render(request, 'example_app_5/topping_overview.html', {
        'topping_list': topping_list,
    })


def pizza_overview(request):
    """
    List view for Pizza model.
    """
    # Pull models from database.
    pizza_list = models.Pizza.objects.all()

    # Send to template for user display.
    return render(request, 'example_app_5/pizza_overview.html', {
        'pizza_list': pizza_list,
    })

#endregion Overview Views


#region Detail Views

def topping_detail(request, topping_id):
    """
    Displays details of the given Topping.
    """
    # Pull models from database.
    topping = get_object_or_404(models.Topping, id=topping_id)

    # Send to template for user display.
    return render(request, 'example_app_5/topping_detail.html', {
        'topping': topping,
    })


def pizza_detail(request, pizza_id):
    pizza = get_object_or_404(models.Pizza, id=pizza_id)
    topping_set = pizza.toppings.all()

    return render(request, 'example_app_5/pizza_detail.html', {
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
            return HttpResponseRedirect(reverse('example_app_5:topping_detail', args=(topping.id, )))

    # Handle for non-post request.
    return render(request, 'example_app_5/forms/topping.html', {
        'form': form,
    })


def pizza_create(request):
    """
    Form view for creating a new Pizza.
    TODO: ManyToMany intermediary saving seems a bit messy. Probably a better way.
    """
    form = forms.PizzaForm()

    # Check if request is post.
    if request.method == 'POST':
        form = forms.PizzaForm(request.POST)
        if form.is_valid():
            # Save the current Pizza object.
            # Commit is False or else the ManyToMany will attempt to save at the same time.
            # Since we use a custom intermediary, this will automatically fail.
            pizza = form.save(commit=False)
            pizza.save()

            for topping_id in request.POST.getlist('toppings'):
                topping = get_object_or_404(models.Topping, id=topping_id)
                models.PizzaToppingRelationship.objects.create(
                    pizza=pizza,
                    topping=topping,
                )

            # Render response for user.
            return HttpResponseRedirect(reverse('example_app_5:pizza_detail', args=(pizza.id, )))

    # Handle for non-post request.
    return render(request, 'example_app_5/forms/pizza.html', {
        'form': form,
    })

#endregion Create Views


#region Edit Views

def topping_edit(request, topping_id):
    """
    Form view for editing a Topping.
    """
    # Pull models from database.
    topping = get_object_or_404(models.Topping, id=topping_id)
    form = forms.ToppingForm(instance=topping)

    # Check if request is post.
    if request.method == 'POST':
        form = forms.ToppingForm(instance=topping, data=request.POST)
        if form.is_valid():
            form.save()

            # Render response for user.
            return HttpResponseRedirect(reverse('example_app_5:topping_detail', args=(topping.id, )))

    # Send to template for user display.
    return render(request, 'example_app_5/forms/topping.html', {
        'form': form,
        'topping': topping,
    })


def pizza_edit(request, pizza_id):
    """
    Form view for editing a Pizza.
    TODO: ManyToMany intermediary saving seems a bit messy. Probably a better way.
    """
    # Pull models from database.
    pizza = get_object_or_404(models.Pizza, id=pizza_id)
    form = forms.PizzaForm(instance=pizza)

    # Check if request is post.
    if request.method == 'POST':
        form = forms.PizzaForm(instance=pizza, data=request.POST)
        if form.is_valid():
            # Save the current object.
            # Commit is False or else the ManyToMany will attempt to save at the same time.
            # Since we use a custom intermediary, this will automatically fail.
            new_pizza = form.save(commit=False)
            new_pizza.save()

            # Clear old topping values.
            new_pizza.toppings.clear()

            for topping_id in request.POST.getlist('toppings'):
                topping = get_object_or_404(models.Topping, id=topping_id)
                models.PizzaToppingRelationship.objects.create(
                    pizza=pizza,
                    topping=topping,
                )


            # Render response for user.
            return HttpResponseRedirect(reverse('example_app_5:pizza_detail', args=(pizza.id, )))

    # Send to template for user display.
    return render(request, 'example_app_5/forms/pizza.html', {
        'form': form,
        'pizza': pizza,
    })

#endregion Edit Views
