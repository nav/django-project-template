from django.contrib import admin
from integration.models import Config


@admin.register(Config)
class ConfigAdmin(admin.ModelAdmin):
    pass
