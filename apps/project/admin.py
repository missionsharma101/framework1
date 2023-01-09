from django.contrib import admin

from apps.project.models import *

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class UserModelAdmin(BaseUserAdmin):
    # The forms to add and change user instances

    list_display = ('id', 'email', 'name', 'tc','is_admin')
    list_filter = ('is_admin', )
    fieldsets = (
        (None, {
            'fields': ('email', 'password')
        }),
        ('Personal info', {
            'fields': ('name', 'tc')
        }),
        ('Permissions', {
            'fields': ('is_admin', )
        }),
    )

    add_fieldsets = ((None, {
        'classes': ('wide', ),
        'fields': ('email', 'name', 'password1', 'password2','tc'),
    }), )
    search_fields = ('email', )
    ordering = ('email', 'id')
    filter_horizontal = ()


# Now register the new UserAdmin...
admin.site.register(CustomUser, UserModelAdmin)
