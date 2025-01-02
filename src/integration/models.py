# integration/models.py

from django.db import models
from infrastructure.models import Audited, Deactivatable


class Config(Audited, Deactivatable):
    name = models.CharField(max_length=100, unique=True)
    config = models.JSONField(default=dict)

    def __str__(self):
        return self.name

    def get(self, key, default=None):
        return self.config.get(key, default)

    def set(self, key, value):
        self.config[key] = value
        self.save()

    def update_config(self, new_config):
        self.config.update(new_config)
        self.save()
