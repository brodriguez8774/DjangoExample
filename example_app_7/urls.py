"""
Urls for Example App 7.
"""

from django.conf.urls import url

from . import views


app_name = 'example_app_7'
urlpatterns = [
    url(r'^$', views.index, name='index'),
]
