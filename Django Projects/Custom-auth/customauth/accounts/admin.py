from django.contrib import admin
from .models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("email", "full_name", "is_active", "is_staff")
    search_fields = ("email", "full_name")


admin.site.register(CustomUser, CustomUserAdmin)