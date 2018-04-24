"""
Admin View for Example App 2.
"""

from django.contrib import admin

from . import models


admin.site.register(models.Category)
