from django.contrib import admin
from .laisha2.models import Material
from .models import VersionModel


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('name', 'level', 'attribute', 'type')


@admin.register(VersionModel)
class VersionModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'version')
