"""
Views for example app 8.
"""

from django.core import serializers
from django.shortcuts import render


from example_app_1 import models


def index(request):
    """
    Index view.
    """
    # Send to template for user display.
    return render(request, 'example_app_8/index.html')


def category_search(request):
    """
    A view showcasing the use of Django models through react.
    Uses the original category models from example_app_1.
    """
    # Pull models from database.
    categories = models.Category.objects.all()

    # Convert to json format for React.
    json_categories = serializers.serialize('json', categories)

    # Send to template for user display.
    return render(request, 'example_app_8/category_search.html', {
        'categories': categories,
        'json_categories': json_categories,
    })
