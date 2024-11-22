from django.contrib import admin

# Register your models here.
from .models import VpnLink, VpnZfbOrder, VpnZfbPrice


class VpnLinkAdmin(admin.ModelAdmin):
    list_display = ("note", "link", "expiration_time", "status", "level")
    search_fields = ["note", "link"]
    list_filter = ("link", "expiration_time", "status", "created_at")
    ordering = (
        "-status",
        "expiration_time",
    )


class VpnZfbOrderAdmin(admin.ModelAdmin):
    list_display = (
        "link",
        "email",
        "device",
        "month",
        "expiration_time",
        "status",
        "level",
    )
    search_fields = ["email", "link"]
    list_filter = ("link", "expiration_time", "status", "created_at")
    ordering = (
        "-status",
        "expiration_time",
    )


class VpnZfbPriceAdmin(admin.ModelAdmin):
    list_display = ("price", "level", "name", "status", "created_at")
    search_fields = ["name"]
    list_filter = ("price", "status", "created_at")
    ordering = ("price",)  # 使用price由小到大的排列


admin.site.register(VpnLink, VpnLinkAdmin)
admin.site.register(VpnZfbOrder, VpnZfbOrderAdmin)
admin.site.register(VpnZfbPrice, VpnZfbPriceAdmin)
