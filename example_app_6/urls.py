"""
Urls for Example App 6.
"""

from django.conf.urls import url

from . import views


app_name = 'example_app_6'
urlpatterns = [
    url(r'^$', views.index, name='index'),

    # Ajax Requests.
    url(r'^ajax/number/$', views.ajax_get_number, name='ajax_get_number'),
]
