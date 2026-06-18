from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model        = CustomUser
    list_display  = ('email', 'first_name', 'last_name', 'user_type', 'student_id', 'is_staff', 'is_active')
    list_filter   = ('user_type', 'is_staff', 'is_active')
    ordering      = ('email',)
    search_fields = ('email', 'first_name', 'last_name', 'student_id')

    fieldsets = (
        (None,            {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'user_type', 'student_id')}),
        ('Permissions',   {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Dates',         {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields':  ('email', 'first_name', 'last_name', 'user_type', 'student_id', 'password1', 'password2'),
        }),
    )
