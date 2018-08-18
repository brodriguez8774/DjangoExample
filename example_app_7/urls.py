"""
Urls for Example App 7.
"""

from django.conf.urls import url

from . import views


app_name = 'example_app_7'
urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^category/search/$', views.category_search, name='category_search'),
    url(r'^category/create/$', views.category_create, name='category_create'),
    url(r'^category/edit/category_pk/$', views.category_edit, name='category_edit_js'),
    url(r'^category/edit/(?P<pk>[0-9]+)/$', views.category_edit, name='category_edit'),
]
