from django.contrib import admin
from .models import Network, Company, Location, Stations, Extra, Payment


class NetworkAdmin(admin.ModelAdmin):

    list_display = ("id", "network_id", "name", "gbfs_href", "href", "created_at")
    search_fields = ("network_id", "name",)
    list_filter = ("created_at",)
    filter_horizontal = ('company',)


class CompanyAdmin(admin.ModelAdmin):

    list_display = ("id", "name", "created_at")
    search_fields = ("id", "name",)
    list_filter = ("created_at",)


class LocationAdmin(admin.ModelAdmin):

    list_display = ("id", "country", "city", "latitude", "longitude", "created_at")
    search_fields = ("id", "country", "city",)
    list_filter = ("created_at",)


class StationsAdmin(admin.ModelAdmin):

    list_display = ("id", "name", "free_bikes", "empty_slots",  "latitude", "longitude", "created_at")
    search_fields = ("id", "name",)
    list_filter = ("created_at",)


class ExtraAdmin(admin.ModelAdmin):

    list_display = ("id", "uid", "altitude", "ebikes", "has_ebikes", "normal_bikes", "payment_terminal", "slots",
                    "returning", "renting",  "updated_at")
    search_fields = ("id", "uid",)
    list_filter = ("updated_at", "has_ebikes", "payment_terminal",)
    filter_horizontal = ('payment',)


class PaymentAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created_at")
    search_fields = ("name",)
    list_filter = ("created_at",)


admin.site.register(Network, NetworkAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Stations, StationsAdmin)
admin.site.register(Extra, ExtraAdmin)
admin.site.register(Payment, PaymentAdmin)
