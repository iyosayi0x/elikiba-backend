from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin
from django.contrib.auth.models import Group

from .forms import UserChangeForm, UserCreationForm

User = get_user_model()


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ("id", "email", "first_name", "last_name")
    list_filter = ("is_active", "is_staff")
    fieldsets = (
        (None, {"fields": ("first_name", "last_name",
         "email", "password", "profile_image")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "last_login",
                    "groups",
                    "user_permissions",
                )
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "email",
                    "password1",
                    "password2",
                )
            },
        ),
    )
    search_fields = ("email", "first_name", "last_name",)
    ordering = ("email",)
    filter_horizontal = ("groups", "user_permissions")

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser
        if is_superuser:
            form.base_fields["is_superuser"].disabled = True
        return form


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
