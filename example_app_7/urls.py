"""
Urls for Example App 7.
"""

from django.conf.urls import url

from . import views


app_name = 'example_app_7'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^category_search/$', views.category_search, name='category_search'),
]
