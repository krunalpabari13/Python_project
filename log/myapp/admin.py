from django.contrib import admin
from .models import registration
class showuser(admin.ModelAdmin):
    list_display = ["name","email","password","date","id"]

# Register your models here.
admin.site.register(registration,showuser)