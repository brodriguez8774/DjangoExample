"""
Urls for Example App 4.
"""

from django.conf.urls import url

from . import views


app_name = 'example_app_4'
urlpatterns = [
    url(r'^$', views.index, name='index'),

    # Overview Views.
    url(r'^topping/$', views.topping_overview, name='topping_overview'),
    url(r'^pizza/$', views.pizza_overview, name='pizza_overview'),

    # Detail Views.
    url(r'^topping/detail/(?P<pk>[0-9]+)/$', views.topping_detail, name='topping_detail'),
    url(r'^pizza/detail/(?P<pk>[0-9]+)/$', views.pizza_detail, name='pizza_detail'),

    # Create Views.
    url(r'^topping/create/$', views.topping_create, name='topping_create'),
    url(r'^pizza/create/$', views.pizza_create, name='pizza_create'),

    # Edit Views.
    url(r'^topping/edit/(?P<pk>[0-9]+)/$', views.topping_edit, name='topping_edit'),
    url(r'^pizza/edit/(?P<pk>[0-9]+)/$', views.pizza_edit, name='pizza_edit'),
]
