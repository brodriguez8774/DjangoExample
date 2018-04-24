"""
Urls for Example App 1.
"""

from django.conf.urls import url

from . import views

app_name = 'example_app_1'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^detail/(?P<category_id>[0-9]+)/$', views.category_detail, name='category_detail'),
    url(r'^create/$', views.category_create, name='category_create'),
    url(r'^edit/(?P<category_id>[0-9]+)/$', views.category_edit, name='category_edit'),
]
