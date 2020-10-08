from django.contrib import admin

from .models import Reference


@admin.register(Reference)
class ReferenceAdmin(admin.ModelAdmin):
    """
    Display Reference in admin.
    """

    list_display = ("__str__",)
    list_filter = (
        "from_currency",
        "to_currency",
    )
