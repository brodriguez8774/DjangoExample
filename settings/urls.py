"""
Core project Urls.
"""

from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    # Admin Views.
    url(r'^admin/', admin.site.urls),

    # Example App 1 Views.
    url(r'^ex1/', include('example_app_1.urls')),

    # Example App 2 Views.
    url(r'^ex2/', include('example_app_2.urls')),

    # Example App 3 Views.
    url(r'^ex3/', include('example_app_3.urls')),

    # Example App 4 Views.
    url(r'^ex4/', include('example_app_4.urls')),

    # Example App 5 Views.
    url(r'^ex5/', include('example_app_5.urls')),

    # Example App 6 Views.
    url(r'^ex6/', include('example_app_6.urls')),

    # Example App 7 Views.
    url(r'^ex7/', include('example_app_7.urls')),

    # Example App 8 Views.
    url(r'^ex8/', include('example_app_8.urls')),
]
