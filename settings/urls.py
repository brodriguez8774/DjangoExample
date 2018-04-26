"""settings URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
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
]
