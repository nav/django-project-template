import pytest
from tenant.factories import TenantFactory, UserFactory


@pytest.fixture
def tenant():
    return TenantFactory()


@pytest.fixture
def user():
    return UserFactory()
