from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import CustomUser
# Register your models here.
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    # fields = ['customer_cnic', 'customer_dob']
    list_display = ['username', 'email', 'is_staff']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'customer_cnic', 'customer_dob')}),
        (('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'customer_cnic', 'customer_dob', 'first_name'),
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)
