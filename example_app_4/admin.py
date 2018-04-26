"""
Admin views for Example App 4.
"""

from django.contrib import admin

from . import forms, models


class PizzaToppingRelationshipInline(admin.TabularInline):
    """
    An inline to represent the Many-to-Many relationship. Will be used in the Pizza model admin.
    """
    model = models.PizzaToppingRelationship
    extra = 1


class ToppingAdmin(admin.ModelAdmin):
    form = forms.ToppingAdminForm

    # Fields to display in admin list view.
    list_display = (
        'name',
    )

    # Fields to search in admin list view.
    search_fields = [
        'name',
    ]

    # Read only fields for admin detail view.
    readonly_fields = (
        'date_created', 'date_modified',
    )

    # Organize fieldsets for admin detail view.
    fieldsets = (
        (None, {
            'fields': ('name',)
        }),
        ('Advanced', {
            'classes': ('collapse',),
            'fields': ('date_created', 'date_modified',),
        })
    )


class PizzaAdmin(admin.ModelAdmin):
    form = forms.PizzaAdminForm
    inlines = (PizzaToppingRelationshipInline,)

    # Fields to display in admin list view.
    list_display = (
        'name',
        'price',
    )

    # Fields to search in admin list view.
    search_fields = [
        'name',
        'price',
        'toppings__name',
    ]

    # Read only fields for admin detail view.
    readonly_fields = (
        'price', 'date_created', 'date_modified',
    )

    # Organize fieldsets for admin detail view.
    fieldsets = (
        (None, {
            'fields': ('name', 'price',)
        }),
        ('Advanced', {
            'classes': ('collapse',),
            'fields': ('date_created', 'date_modified',),
        })
    )


admin.site.register(models.Topping, ToppingAdmin)
admin.site.register(models.Pizza, PizzaAdmin)
