"""
Views for Example App 2.
"""


from django.views import generic

from . import forms, models


class IndexView(generic.ListView):
    """
    Index view. Displays all current category models.
    """
    template_name = 'example_app_2/index.html'

    def get_queryset(self):
        # You don't need to define what the list will be called in the template.
        # By returning a model, Django automatically uses "'model_name'_list" as the return.
        # So in this instance, it will be "category_list" by default.
        return models.Category.objects.all()


class DetailView(generic.DetailView):
    """
    Displays details of the given category.
    """
    model = models.Category
    template_name = 'example_app_2/category_detail.html'


class CategoryCreate(generic.edit.CreateView):
    """
    Form view for creating a new Category.
    """
    model = models.Category
    form_class = forms.CategoryForm
    template_name = "example_app_2/forms/category.html"


class CategoryUpdate(generic.edit.UpdateView):
    """
    Form view for editing a Category.
    """
    model = models.Category
    form_class = forms.CategoryForm
    template_name = "example_app_2/forms/category.html"
