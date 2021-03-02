from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from django.utils.translation import gettext_lazy


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    # 列表显示字段
    list_display = ('username', 'email', 'nickname', 'is_staff')
    # 修改页面的显示字段
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (gettext_lazy('Personal info'), {'fields': ('nickname', 'email')}),
        (gettext_lazy('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (gettext_lazy('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
