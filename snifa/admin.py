from django.contrib import admin
from .models import Snifa


class SnifaAdmin(admin.ModelAdmin):
    list_display = ("id", "file", "auditable_unit", "auditable_unit_url", "company_name",  "category",
                    "region", "state", "detail_url", "created_at")
    search_fields = ("file", "category", "region", "state",)
    list_filter = ("created_at",)


admin.site.register(Snifa, SnifaAdmin)
