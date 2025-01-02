from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.sites.models import Site
from django.utils.translation import gettext_lazy as _

from tenant.models import Membership, Tenant, User, Invite


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    exclude = ("user_id",)
    readonly_fields = ("user_id",)
    search_fields = ("user_id", "username", "first_name", "last_name", "email")

    fieldsets = (
        (None, {"fields": ("user_id", "username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )

    filter_horizontal = ("user_permissions",)


@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    pass


class TenantAdmin(admin.StackedInline):
    model = Tenant
    exclude = ("tenant_id",)
    readonly_fields = ("tenant_id",)


admin.site.unregister(Site)


@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    inlines = (TenantAdmin,)
    list_display = ("domain", "name")
    search_fields = ("domain", "name")


@admin.register(Invite)
class InviteAdmin(admin.ModelAdmin):
    pass
