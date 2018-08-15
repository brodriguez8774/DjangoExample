"""
Views for example app 7.
"""


from django.shortcuts import render


def index(request):
    """
    Index view.
    """
    # Send to template for user display.
    return render(request, 'example_app_7/index.html')
