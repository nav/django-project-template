from django.db import models
from django.utils.translation import gettext_lazy as _


class Audited(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Date and time when the object was created.",
        verbose_name="Created At",
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Date and time when the object was last updated.",
        verbose_name="Updated At",
    )

    class Meta:
        abstract = True


class DeactivatableManager(models.Manager):
    """Custom manager that allows soft deletion/deactivation"""

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class Deactivatable(models.Model):
    is_active = models.BooleanField(default=True)

    objects = models.Manager()
    active_objects = DeactivatableManager()

    class Meta:
        abstract = True

    def deactivate(self):
        self.is_active = False
        self.save(update_fields=["is_active"])
