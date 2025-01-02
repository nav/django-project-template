from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser, Group
from django.utils.translation import gettext_lazy as _
from infrastructure.fields import UlidField
from infrastructure.models import Audited, Deactivatable, DeactivatableManager


def tenant_logo_destination(instance, filename):
    return "/".join([instance.tenant_id, "logo", filename])


class TenantManager(DeactivatableManager):
    def for_domain(self, domain: str):
        return self.get_queryset().select_related("site").get(site__domain=domain)


class Tenant(Audited, Deactivatable):
    tenant_id = UlidField(prefix="tnt_")
    site = models.OneToOneField("sites.Site", on_delete=models.CASCADE)

    objects = models.Manager()
    active_objects = TenantManager()

    def __str__(self):
        return f"Tenant domain={self.site.domain}"


class TenantedManager(DeactivatableManager):
    def for_tenant(self, tenant: Tenant):
        return self.get_queryset().select_related("tenant").filter(tenant=tenant)


class Tenanted(Deactivatable):
    tenant = models.ForeignKey(
        "tenant.Tenant", on_delete=models.CASCADE, related_name="+"
    )

    objects = models.Manager()
    active_objects = TenantedManager()

    class Meta:
        abstract = True


class User(AbstractUser, Deactivatable):
    user_id = UlidField(prefix="usr_")
    groups = models.ManyToManyField(
        Group,
        through="Membership",
        verbose_name=_("groups"),
        blank=True,
        help_text=_(
            "The groups this user belongs to. A user will get all permissions "
            "granted to each of their groups."
        ),
        related_name="user_set",
        related_query_name="user",
    )


class Membership(Audited, Tenanted):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return f"Membership tenant={self.tenant_id} user={self.user_id} group={self.group_id}"


class Invite(Audited, Tenanted):
    inviter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    email = models.EmailField(db_index=True)
    groups = models.ManyToManyField(Group)

    def __str__(self):
        return f"Invite email={self.email} inviter={self.inviter}"
