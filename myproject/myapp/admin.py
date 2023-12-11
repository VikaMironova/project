from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import MyModel


class MyModelAdmin(MPTTModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(MyModel, MyModelAdmin)
