from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ("username", "email", "is_business", "grade")
    fieldsets = (
        (None, {"fields": ("username", "password", "is_business", "grade")}),
        # (("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        # (
        #     ("Permissions"),
        #     {
        #         "fields": (
        #             "is_active",
        #             "is_staff",
        #             "is_superuser",
        #             "groups",
        #             "user_permissions",
        #         ),
        #     },
        # ),
        (("Important dates"), {"fields": ("last_login", "date_joined")}),
    )