from django.contrib import admin

# Register your models here.
from .models import VpnLink


class VpnLinkAdmin(admin.ModelAdmin):
    list_display = ("note", "link", "expiration_time", "status")
    search_fields = ["note", "link"]
    list_filter = ("created_at", "link", "expiration_time")


admin.site.register(VpnLink, VpnLinkAdmin)
