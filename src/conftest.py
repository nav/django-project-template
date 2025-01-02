import pytest
import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage


fss = FileSystemStorage()


@pytest.fixture(autouse=True)
def enable_db_access(db):
    pass


@pytest.fixture(scope="session")
def django_db_setup(django_db_setup):
    settings.DATABASES["default"] = {
        "ENGINE": "django.db.backends.postgresql",
        "ATOMIC_REQUESTS": True,
        "NAME": os.getenv("TEST_DB_NAME", "test_app"),
        "OPTIONS": {
            "service": "app_service",
            "passfile": settings.BASE_DIR.parent / ".pgpass",
        },
    }
