"""
Views for Example App 2.
"""

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from . import forms, models

class IndexView(generic.ListView):
    template_name = 'example_app_2/index.html'

    def get_queryset(self):
        # You don't need to define what the list will be called in the template.
        # By returning a model, Django automatically uses "'model_name'_list" as the return.
        # So in this instance, it will be "category_list" by default.
        return models.Category.objects.all()


class DetailView(generic.DetailView):
    model = models.Category
    template_name = 'example_app_2/category_detail.html'


class CategoryCreate(generic.edit.CreateView):
    model = models.Category
    form_class = forms.CategoryForm
    template_name = "example_app_2/forms/category.html"



class CategoryUpdate(generic.edit.UpdateView):
    model = models.Category
    form_class = forms.CategoryForm
    template_name = "example_app_2/forms/category.html"
