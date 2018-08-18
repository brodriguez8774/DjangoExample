"""
Views for Example App 1.
"""

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from . import forms, models


def index(request):
    """
    Index view. Displays all current category models.
    """
    # Pull models from database.
    category_list = models.Category.objects.all()

    # Send to template for user display.
    return render(request, 'example_app_1/index.html', {
        'category_list': category_list,
    })


def category_detail(request, category_id):
    """
    Displays details of the given category.
    """
    # Pull models from database.
    category = get_object_or_404(models.Category, id=category_id)

    # Send to template for user display.
    return render(request, 'example_app_1/category_detail.html', {
        'category': category,
    })


def category_create(request):
    """
    Form view for creating a new Category.
    """
    # Note that a blank form is loaded before everything else.
    # This ensures that, on a POST error, all data is returned to user on page load.
    form = forms.CategoryForm()
    # Check if request is post.
    if request.method == 'POST':
        form = forms.CategoryForm(request.POST)
        if form.is_valid():
            category = form.save()

            # Render response for user.
            return HttpResponseRedirect(reverse('example_app_1:category_detail', args=(category.pk, )))

    # Handle for non-post request.
    return render(request, 'example_app_1/forms/category.html', {
        'form': form,
    })


def category_edit(request, category_id):
    """
    Form view for editing a Category.
    """
    # Pull models from database.
    category = get_object_or_404(models.Category, id=category_id)
    form = forms.CategoryForm(instance=category)

    # Check if request is post.
    if request.method == 'POST':
        form = forms.CategoryForm(instance=category, data=request.POST)
        if form.is_valid():
            form.save()

            # Render response for user.
            return HttpResponseRedirect(reverse('example_app_1:category_detail', args=(category.pk, )))

    # Send to template for user display.
    return render(request, 'example_app_1/forms/category.html', {
        'form': form,
        'category': category,
    })
