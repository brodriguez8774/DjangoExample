"""
Views for Example App 2.
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
    return render(request, 'example_app_2/index.html', {
        'category_list': category_list,
    })


def category_detail(request, category_id):
    """
    Displays details of the given category.
    """
    # Pull models from database.
    category = get_object_or_404(models.Category, id=category_id)

    # Send to template for user display.
    return render(request, 'example_app_2/category_detail.html', {
        'category': category,
    })


def category_create(request):
    """
    Form view for creating a new Category.
    """
    # Check if request is post.
    if request.method == 'POST':
        form = forms.CategoryForm(request.POST)
        if form.is_valid():
            category = form.save()

            # Render response for user.
            return HttpResponseRedirect(reverse('example_app_2:category_detail', args=(category.id, )))

    # Handle for non-post request.
    form = forms.CategoryForm()
    return render(request, 'example_app_2/forms/category.html', {
        'form': form,
    })


def category_edit(request, category_id):
    """
    Form view for editing a Category.
    """
    # Pullmodels from database.
    category = get_object_or_404(models.Category, id=category_id)
    form = forms.CategoryForm(instance=category)

    # Check if request is post.
    if request.method == 'POST':
        form = forms.CategoryForm(instance=category, data=request.POST)
        if form.is_valid():
            form.save()

            # Render response for user.
            return HttpResponseRedirect(reverse('example_app_2:category_detail', args=(category.id, )))

    # Send to template for user display.
    return render(request, 'example_app_2/forms/category.html', {
        'form': form,
        'category': category,
    })