"""
Views for example app 7.
"""

from django.core import serializers
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from . import forms, models


def index(request):
    """
    Index view.
    """
    # Send to template for user display.
    return render(request, 'example_app_7/index.html')


def category_search(request):
    """
    A view showcasing the use of Django models through react.
    """
    # Pull models from database.
    categories = models.Category.objects.all()

    # Convert to json format for React.
    json_categories = serializers.serialize(
        'json',
        categories,
        fields=('title', 'date_created', 'date_modified', 'url')
    )

    # Send to template for user display.
    return render(request, 'example_app_7/category_search.html', {
        'categories': categories,
        'json_categories': json_categories,
    })


def category_create(request):
    """
    Form view for creating a new Category.
    """
    form = forms.CategoryForm()

    # Check if request is post.
    if request.method == 'POST':
        form = forms.CategoryForm(request.POST)
        if form.is_valid():
            category = form.save()

            # Render response for user.
            return HttpResponseRedirect(reverse('example_app_7:category_search'))

    # Handle for non-post request.
    return render(request, 'example_app_7/category_form.html', {
        'form': form,
    })


def category_edit(request, pk):
    """
    Form view for editing a Category.
    """
    category = get_object_or_404(models.Category, id=pk)
    form = forms.CategoryForm(instance=category)

    # Check if request is post.
    if request.method == 'POST':
        form = forms.CategoryForm(instance=category, data=request.POST)
        if form.is_valid():
            form.save()

            # Render response for user.
            return HttpResponseRedirect(reverse('example_app_7:category_search'))

    # Send to template for user display.
    return render(request, 'example_app_7/category_form.html', {
        'form': form,
        'category': category,
    })
