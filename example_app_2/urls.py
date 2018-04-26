"""
Urls for Example App 2.
"""


from django.conf.urls import url

from . import views


app_name = 'example_app_2'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^detail/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='category_detail'),
    url(r'^create/$', views.CategoryCreate.as_view(), name='category_create'),
    url(r'^edit/(?P<pk>[0-9]+)/$', views.CategoryUpdate.as_view(), name='category_edit'),
]
