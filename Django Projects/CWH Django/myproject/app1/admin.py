from django.contrib import admin
from app1.models import contact

# Register your models here.


class contactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email' , 'phone')
    search_fields = ('name', 'email')
    

admin.site.register(contact , contactAdmin)