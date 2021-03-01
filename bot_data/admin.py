from django.contrib import admin
from .laisha2.models import Material


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('name', 'level', 'attribute', 'type')
