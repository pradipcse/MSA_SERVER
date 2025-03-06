from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'name', 'is_staff', 'is_superuser', 'is_active', 'date_time_of_creation')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    ordering = ('-date_time_of_creation',)  # Newest users first
    search_fields = ('email', 'name')

    fieldsets = (
        (None, {'fields': ('email', 'name', 'password', 'is_verified', 'verification_token')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser', 'is_active', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('date_time_of_creation',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'password1', 'password2', 'is_verified', 'is_staff', 'is_superuser', 'is_active')}
        ),
    )

    actions = ['delete_selected_users']

    def delete_selected_users(self, request, queryset):
        """ Custom action to delete selected users """
        deleted_count, _ = queryset.delete()
        self.message_user(request, f'{deleted_count} user(s) were successfully deleted.')
    delete_selected_users.short_description = "Delete selected users"

admin.site.register(CustomUser, CustomUserAdmin)
