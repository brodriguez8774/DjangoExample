"""
Urls for Example App 3.
"""


from django.conf.urls import url

from . import views


app_name = 'example_app_3'
urlpatterns = [
    url(r'^$', views.index, name='index'),

    # Overview Views.
    url(r'^address/$', views.address_overview, name='address_overview'),
    url(r'^customer/$', views.customer_overview, name='customer_overview'),

    # Detail Views.
    url(r'^address/detail/(?P<address_id>[0-9]+)/$', views.address_detail, name='address_detail'),
    url(r'^customer/detail/(?P<customer_id>[0-9]+)/$', views.customer_detail, name='customer_detail'),

    # Create Views.
    url(r'^address/create/$', views.address_create, name='address_create'),
    url(r'^customer/create/$', views.customer_create, name='customer_create'),

    # Edit Views.
    url(r'^address/edit/(?P<address_id>[0-9]+)/$', views.address_edit, name='address_edit'),
    url(r'^customer/edit/(?P<customer_id>[0-9]+)/$', views.customer_edit, name='customer_edit'),
]
