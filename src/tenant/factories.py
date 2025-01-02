import factory
from factory.django import DjangoModelFactory
from infrastructure.factories import BaseAddressFactory


class SiteFactory(DjangoModelFactory):
    domain = factory.Sequence(lambda n: f"site{n}.example.com")
    name = factory.Sequence(lambda n: f"Site {n}")

    class Meta:
        model = "sites.Site"


class TenantFactory(BaseAddressFactory):
    site = factory.SubFactory(SiteFactory)

    class Meta:
        model = "tenant.Tenant"


class TenantedFactory(DjangoModelFactory):
    tenant = factory.SubFactory(TenantFactory)


class UserFactory(DjangoModelFactory):
    class Meta:
        model = "tenant.User"


class MembershipFactory(DjangoModelFactory):
    class Meta:
        model = "tenant.Membership"


class InviteFactory(DjangoModelFactory):
    class Meta:
        model = "tenant.Invite"
