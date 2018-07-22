"""
Views for Example App 6.
"""

import random
from django.shortcuts import render
from django.http import JsonResponse


def index(request):
    """
    Index view.
    """
    # Send to template for user display.
    return render(request, 'example_app_6/index.html')


def ajax_get_number(request):
    """
    Sends an ajax request of a random number between 1 and 10.
    """
    rand_number = random.randint(1, 10)
    # Send to template for user display.
    return JsonResponse({
        'value': 'Ajax request received!',
        'rand_number': rand_number,
    })
