"""
Admin views for Example App 3.
"""


from django.contrib import admin

from . import forms, models


class AddressAdmin(admin.ModelAdmin):
    form = forms.AddressAdminForm

    # Fields to display in admin list view.
    list_display = (
        'address',
    )

    # Fields to search in admin list view.
    search_fields = [
        'address',
    ]

    # Read only fields for admin detail view.
    readonly_fields = (
        'date_created', 'date_modified',
    )

    # Organize fieldsets for admin detail view.
    fieldsets = (
        (None, {
            'fields': ('address',)
        }),
        ('Advanced', {
            'classes': ('collapse',),
            'fields': ('date_created', 'date_modified',),
        })
    )


class CustomerAdmin(admin.ModelAdmin):
    form = forms.CustomerAdminForm

    def full_name(self, instance):
        """
        Calls the function defined in model on the current model instance to get the full name value.
        Essentially concatenates first and last name into one single field.
        """
        return instance.get_full_name()

    # Fields to display in admin list view.
    list_display = (
        'full_name', # Note, this uses the above function to display both first and last as one column.
        'address',
    )

    # Fields to search in admin list view.
    search_fields = [
        'first_name',
        'last_name',
        'address',
    ]

    # Read only fields for admin detail view.
    readonly_fields = (
        'date_created', 'date_modified',
    )

    # Organize fieldsets for admin detail view.
    fieldsets = (
        (None, {
            'fields': ('first_name', 'last_name', 'address',)
        }),
        ('Advanced', {
            'classes': ('collapse',),
            'fields': ('date_created', 'date_modified',),
        })
    )


admin.site.register(models.Address, AddressAdmin)
admin.site.register(models.Customer, CustomerAdmin)
