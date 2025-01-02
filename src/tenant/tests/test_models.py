from django.contrib.auth import get_user_model

from tenant.factories import TenantFactory
from tenant.models import Tenant, TenantManager

User = get_user_model()


class TestTenantModel:
    def test_tenant_is_active_by_default(self, tenant):
        assert tenant.is_active is True

    def test_tenant_can_be_deactivated(self, tenant):
        tenant.deactivate()
        assert tenant.is_active is False

    def test_get_tenant_manager(self):
        manager = Tenant.active_objects
        assert isinstance(manager, TenantManager)

    def test_get_tenant_by_domain(self):
        tenant1 = TenantFactory(site__domain="a.com")
        tenant2 = TenantFactory(site__domain="b.org")
        assert Tenant.active_objects.for_domain("a.com") == tenant1
        assert Tenant.active_objects.for_domain("b.org") == tenant2

        assert str(tenant1) == "Tenant domain=a.com"


class TestUserModel:
    def test_user_is_active_by_default(self, user):
        assert user.is_active is True

    def test_user_can_be_deactivated(self, user):
        user.deactivate()
        assert user.is_active is False
        assert not get_user_model().active_objects.filter(pk=user.pk).exists()
